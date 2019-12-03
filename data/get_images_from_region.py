# get spots for all of california
# GET https://services.surfline.com/taxonomy?type=taxonomy&id=58f7ed51dadb30820bb387a6&maxDepth=2

# filter for each record in "contains", r["type"] == "spot"

# for each of those spots, grab their spot ID (r["spot"])

# using the batch endpoint, grab region overviews for each spot
# POST https://services.surfline.com/kbyg/spots/batch
# body: { spotIds: ["", ...] }
# response: {..., "data": [{..., cameras: []}, ...]}

# for each spot with any cameras, grab one frame from spots' cameras' rewindUrl
# save each image in PNG format in the "images" folder like "{spot_id}.png"

