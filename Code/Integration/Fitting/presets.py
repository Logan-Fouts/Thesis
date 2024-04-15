import sys
import os

# create path from current file-path 
current_script_dir = os.path.dirname(os.path.abspath(__file__))
algorithms_dir = os.path.normpath(os.path.join(current_script_dir, '..', '..', 'Algorithms'))

# append Algorithms to sys.path for sake of import
if algorithms_dir not in sys.path:
  sys.path.append(algorithms_dir)

from Dhash.dhash import Dhash
from Phash.phash import Phash
from SIFT.sift import SIFT
from VGG.vgg import VGG

# TODO fill this list as you get better results 
presets = {
  "minhash": { # not implemented yet..
    "low": [],
    "high": [],
  },
  "dhash": {
    "low": [15],
    "high": [15]
  },
  "phash": {
    "low": [15],
    "high": [15]
  },
  "sift": {
    "low": [40, 0.35],
    "high": [40, 0.35]
  },
  "vgg": {
    "low": [0.6],
    "high": [0.6]
  }
}

algorithms = {
  "dhash": Dhash,
  "phash": Phash,
  "sift": SIFT,
  "vgg": VGG
}