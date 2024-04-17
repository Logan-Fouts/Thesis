import argparse
import os
import sys

project_root = os.path.dirname(os.path.abspath(__file__))
algorithms_path = os.path.join(project_root, "Algorithms")
integration_path = os.path.join(project_root, "Integration")

sys.path.append(algorithms_path)
sys.path.append(integration_path)

from Dhash.dhash import Dhash
from Layers.layers import Layers
from Phash.phash import Phash
from SIFT.sift import SIFT
from VGG.vgg import VGG


def get_image_paths(directory):
    """
    Recursively grabs image paths from directory and stores in an array.
    """
    paths = []
    extensions = {".jpg", ".jpeg", ".png"}

    for root, _, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1].lower() in extensions:
                paths.append(os.path.join(root, file))

    return paths


algorithm_map = {
  "dhash": Dhash,
  "phash": Phash,
  "sift": SIFT,
  "vgg": VGG
}

# def combine(dataset, layer_size = 3, options = "all"):
  
#   echo "to be implemented"

# helper functions 
def test_setting(settings, dataset):
  layers = []

  # building layered algorithm based on setting
  for setting in settings:
    print(f'adding layer:{setting["name"]}, mode={setting["mode"]}')
    # get the algorithm from MAP (defined in presets.py)
    algorithm_class = algorithm_map[setting["name"]]
    if algorithm_class:
      # now get the params based on mode (low | high)
      params = presets[setting["name"]][setting["mode"]]

      if params:
        # finally we build our layered algorithm 
        layers.append(algorithm_class(*params))

  

  # create our architecture
  layered_architecture = Layers(layers)
  layered_architecture.run(dataset['paths'])

  # we want to get the groups of which the images belongs too (as )
  preprocessed_results = preprocess_results(layered_architecture)

  true_positives = 0
  false_positives = 0
  print("results made", preprocessed_results)

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
    

def main2():
  filepath = os.path.normpath(os.path.join(current_script_dir, "../../datasets/timelapse/multiple-timelapse/highfit.dataset.json", ))
  
  # Open the file and parse the JSON
  with open(filepath, 'r') as file:
    dataset = json.load(file)
  
  tp, fp = test_setting([{'name':"dhash", 'mode': "low"}, {'name':"dhash", 'mode':"high"}], dataset['03'])

  print(f"TP:{tp}, FP:{fp}")

main2()


def main(image_dir, layers_list):
    """
    Takes args and runs specified layered architecture.
    """
    image_paths = get_image_paths(image_dir)

    available_layers = {
        "Phash": Phash(),
        "Dhash": Dhash(),
        "VGG": VGG(),
        "SIFT": SIFT(),
    }

    layers = [
        available_layers[layer] for layer in layers_list if layer in available_layers
    ]

    if not layers:
        layers = [Phash(), Dhash(), VGG(), SIFT()]  # Normal case

    layered_architecture = Layers(layers)
    layered_architecture.run(image_paths)
    layered_architecture.print_final_results()


# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Find duplicate images.")
#     parser.add_argument(
#         "folder_path", type=str, help="Path to the folder containing images."
#     )
#     parser.add_argument(
#         "-l",
#         "--layers",
#         nargs="+",
#         help="List of layers to use in order (e.g., Phash Dhash VGG SIFT)",
#         default=[],
#     )
#     args = parser.parse_args()
#     main(args.folder_path, args.layers)
