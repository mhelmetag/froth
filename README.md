# froth

Image segmentation for surfcams

## Data

### Info

Image gathering is done by region through the batch region API. From there, images are pulled from each cams rewind clip.

The images are unaltered PNGs and labeled by spot ID.

The masks (aka labels) are class coded PNGs (0 - Sky, 1 - Ocean, 2 - Ground) and also labeled by spot ID.

### Setup

General requirements are:

- ffmpeg
- pipenv
- python3

Then:

```sh
$ pipenv install
$ pipenv shell
```

## ML

TBD
