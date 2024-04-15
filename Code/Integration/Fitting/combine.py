import sys
import os

# create path from current file-path 
current_script_dir = os.path.dirname(os.path.abspath(__file__))
algorithms_dir = os.path.normpath(os.path.join(current_script_dir, '..', '..', 'Algorithms'))
integration_dir = os.path.normpath(os.path.join(current_script_dir, '..', '..', 'Integration'))

# append directories to sys.path for sake of import
if algorithms_dir not in sys.path:
  sys.path.append(algorithms_dir)

if integration_dir not in sys.path:
  sys.path.append(integration_dir)

# import from Algorithms
from Dhash.dhash import Dhash
from Phash.phash import Phash
from SIFT.sift import SIFT
from VGG.vgg import VGG

# import from Integration
from Layers.layers import Layers

# import local
from presets import presets

algorithm_map = {
  "dhash": Dhash,
  "phash": Phash,
  "sift": SIFT,
  "vgg": VGG
}

def test_setting(settings, dataset):
  layers = []

  # building layered algorithm based on setting
  for setting in settings:
    # get the algorithm from MAP (defined in presets.py)
    algorithm_class = algorithm_map.get(setting["name"])
    if algorithm_class:
      # now get the params based on mode (low | high)
      params = presets.get(setting["mode"])
      if params:
        # finally we build our layered algorithm 
        layers.append(algorithm_class(*params))

  # create our architecture
  layered_architecture = Layers(layers)
  layered_architecture.run(dataset["image_paths"])

  # process the results based on dataset
  echo "to be implemented: parsing results based on run and current dataset"

def combine(dataset, layer_size = 3, options = "all"):
  echo "to be implemented"

def showcase():
  echo "to be implemented"