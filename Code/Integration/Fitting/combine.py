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

def combine(dataset, layer_size = 3, options = "all"):
  
  echo "to be implemented"

def showcase():
  echo "to be implemented"

# helper functions 
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
  layered_architecture.run(dataset["paths"])

  # we want to get the groups of which the images belongs too (as )
  preprocessed_results = preprocess_results(layer)

  true_positives = 0
  false_positives = 0

  for group of preprocessed_results:
    if len(group) > 0:
      group_index = dataset['map'][group[0]]

      for path in group:
        if dataset['map'][path] == group_index:
          true_positives += 1
        else:
          false_positives += 1

  return true_positives, false_positivess
        


  # process the results based on dataset
  echo "to be implemented: parsing results based on run and current dataset"
  map_reference = {}
  groups = []

  for touple in layer.result_duplicates:  
    found_group = None 

    a, b = touple
    if not preprocess_results_helper(a, b, map_reference, groups):
      if not preprocess_results_helper(b, a, map_reference, groups):
        # none of the elements exists so we add then both 
        group_index = len(groups)
        groups.append([a, b])
        map_reference[a] = group_index
        map_reference[b] = group_index

  return groups


# this assumes the layer.result_duplicates is a list of touples 
def preprocess_results_helper(a, b, map_reference, groups):
  if a in map_reference:
    if b not in map_reference:
      map_reference[b] = map_reference[a]
      groups[map_reference[a]].append(b)
      return True 

  return False 
    
def preprocess_results(layer):