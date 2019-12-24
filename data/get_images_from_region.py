"""Script for pulling a single frame from Surfline surfcams for a whole region"""

import os
import time
import requests
import ffmpeg

TIMESTAMP = int(time.time())
DATA_DIR = os.path.dirname(__file__)
REGION_ID = "58f7ed51dadb30820bb387a6"  # California
URL = f"https://services.surfline.com/taxonomy?type=taxonomy&id={REGION_ID}&maxDepth=2"


def main():
    taxonomy_response = requests.get(URL)
    json_taxonomy_response = taxonomy_response.json()
    geos = json_taxonomy_response["contains"]

    spots = filter(lambda g: g["type"] == "spot", geos)
    spot_ids = list(map(lambda g: g["spot"], spots))

    batch_overview_response = requests.post(
        "https://services.surfline.com/kbyg/spots/batch", json={"spotIds": spot_ids})
    json_batch_overview_response = batch_overview_response.json()
    json_overviews = json_batch_overview_response["data"]
    json_overviews_with_cameras = filter(
        lambda s: len(s["cameras"]) > 0, json_overviews)

    for json_overview in json_overviews_with_cameras:
        spot_id = json_overview["_id"]
        rewind_url = json_overview["cameras"][0]["rewindClip"]

        ffmpeg_fileformat = os.path.join(
            DATA_DIR, f"images/{TIMESTAMP}_{spot_id}.png")

        stream = ffmpeg.input(rewind_url)
        stream = ffmpeg.output(stream, ffmpeg_fileformat, vframes=1)
        stream.run()

    print("Complete")

main()
