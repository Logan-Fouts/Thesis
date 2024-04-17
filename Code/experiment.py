import sys
import os
import json 
from itertools import permutations

# create path from current file-path 
current_script_dir = os.path.dirname(os.path.abspath(__file__))
algorithms_dir = os.path.normpath(os.path.join(current_script_dir, 'Algorithms'))
integration_dir = os.path.normpath(os.path.join(current_script_dir, 'Integration'))

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

# def combine(dataset, layer_size = 3, options = "all"):
#   echo "to be implemented"

# helper functions 
def test_setting(settings, dataset, size=-1):
  layers = []

  # building layered algorithm based on setting
  for setting in settings:
    # get the algorithm from MAP (defined in presets.py)
    algorithm_class = algorithm_map[setting["name"]]
    if algorithm_class:
      # now get the params based on mode (low | high)
      params = setting["params"]

      if params:
        # finally we build our layered algorithm 
        layers.append(algorithm_class(*params))

  # create our architecture
  layered_architecture = Layers(layers)
  layered_architecture.run(dataset['paths'][:size])

  # we want to get the groups of which the images belongs too (as )
  # preprocessed_results = preprocess_results(layered_architecture)
  preprocessed_results = layered_architecture.group_related_images()

  layered_architecture.print_final_results()

  true_positives = 0
  false_positives = 0

  for group in preprocessed_results:
    if len(group) > 0:
      compare_map = {}

      for path in group:
        if dataset['map'][path] not in compare_map:
          compare_map[dataset['map'][path]] = 0

        compare_map[dataset['map'][path]] += 1

      sorted_compare = sorted(list(compare_map.values()), reverse=True)
      
      # excellent compare 
      true_positives += sorted_compare[0]
      false_positives += sum(sorted_compare[1:])
  
  return true_positives, false_positives
        

def preprocess_results(layer):
  # process the results based on dataset
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


# config = Array<{ name:string, params: Array<number> }>
def compare(dataset, layer_size = 3, dataset_size=-1, config = "all"):

  if config == "all":
    config = []
    for algorithm_name in algorithm_map:
      if presets[algorithm_name]:
        for mode in presets[algorithm_name]:
          config.append({'name': algorithm_name, 'params': presets[algorithm_name][mode] })

  perumation_sets = list(permutations(config, layer_size))

  tp, fp = test_setting([{'name': "phash", 'params': [4]}, {'name': 'dhash', 'params': [3]}, {'name': 'sift', 'params': [17, 1.8, 10000, 3, 0.01]}], dataset, dataset_size)
  print(f"# experiment finished ✅\nTP: {tp}, FP: {fp}")

  # for setting in perumation_sets:
  #   tp, fp = test_setting(setting, dataset, dataset_size)
    # print(f"# experiment finished ✅\nTP: {tp}, FP: {fp}\nset: {setting}")


def get_dataset(path):
  filepath = os.path.normpath(os.path.join(current_script_dir, path))

  # Open the file and parse the JSON
  with open(filepath, 'r') as file:
    dataset = json.load(file)
    return dataset


# dataset defenition 
def timelapse_dataset():
  return get_dataset("datasets/timelapse/multiple-timelapse/highfit.dataset.json")

def finger_print_dataset():
  return get_dataset("datasets/fingerprint/output.json")

dataset = finger_print_dataset()
compare(dataset=dataset, dataset_size=30)