import glob
import json
import os
import os.path as osp

import numpy as np
from PIL import Image

import labelme

ML_DIR = osp.dirname(__file__)
LABELS_FILE = osp.join(ML_DIR, "codes.txt")
IMAGES_DIR = osp.join(ML_DIR, "images")
LABELS_DIR = osp.join(ML_DIR, "labels")

def main():
    class_name_to_id = {}
    for i, line in enumerate(open(LABELS_FILE).readlines()):
        class_id = i - 1
        class_name = line.strip()
        class_name_to_id[class_name] = class_id

    for label_file in glob.glob(osp.join(IMAGES_DIR, '*.json')):
        print('Generating dataset from:', label_file)

        with open(label_file) as f:
            base_filename = osp.splitext(osp.basename(label_file))[0]
            mask_filename = osp.join(LABELS_DIR, base_filename + '.png')

            data = json.load(f)

            img_file = osp.join(osp.dirname(label_file), data['imagePath'])
            img = np.asarray(Image.open(img_file))

            lbl = labelme.utils.shapes_to_label(
                img_shape=img.shape,
                shapes=data['shapes'],
                label_name_to_value=class_name_to_id,
            )

            mask_pil = Image.fromarray(lbl.astype(np.uint8), mode='P')
            mask_pil.save(mask_filename)

    print("Complete")

main()
