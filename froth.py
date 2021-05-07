import sys
from fastai.vision import (
    open_image,
    load_learner
)
from pathlib import Path


path = Path("ml/images")
learn = load_learner(path)

image_path = Path(sys.argv[1])
