import json
import os
import sys
import time
from itertools import permutations

# create path from current file-path
current_script_dir = os.path.dirname(os.path.abspath(__file__))
algorithms_dir = os.path.normpath(os.path.join(current_script_dir, "../Algorithms"))
integration_dir = os.path.normpath(os.path.join(current_script_dir, "../Integration"))

# append directories to sys.path for sake of import
if algorithms_dir not in sys.path:
    sys.path.append(algorithms_dir)

if integration_dir not in sys.path:
    sys.path.append(integration_dir)

# import from Algorithms
from Dhash.dhash import Dhash
# import from Integration
from Layers.layers import Layers
from Phash.phash import Phash
from SIFT.sift import SIFT
from VGG.vgg import VGG

# Open the file and load the data
with open('presets.json', 'r') as file:
    presets = json.load(file)

algorithm_map = {"dhash": Dhash, "phash": Phash, "sift": SIFT, "vgg": VGG}
# algorithm_map = {"dhash": Dhash, "phash": Phash, "sift": SIFT}

# helper functions


def accuracy_calculator(duplicate_groups, non_duplicate_list, lonely_imgs, dataset):
  tp = 0
  fp = 0
  tn = 0
  fn = 0

  for list in duplicate_groups:
    groups = {}

    # keep track of the most common 
    maxmap = {
      'value': 0,
      'index': -1
    }
    for path in list:
      index = dataset['map'][path]

      if index not in groups:
        groups[index] = 0

      groups[index] += 1

      if groups[index] > maxmap['value']:
        maxmap['value'] = groups[index]
        maxmap['index'] = index

    # treat most common group as the main group 
    tp += maxmap['value']

    # put the remaining into false positives 
    for group_index, count in groups.items():
      if group_index != maxmap['index']:
        fp += count 

  # now lets check the tn & fn by checking non_duplicate_list
  for path in non_duplicate_list:
    grouplength = len(dataset['groups'][dataset['map'][path]])
    if grouplength == 1:
      tn += 1
    else:
      fn += 1

  return tp, fp, tn, fn

def test_permutation(foldername, settings, dataset, size=-1, accuracy_calculator=None):
    layers = []

    setting_name = ""
    # building layered algorithm based on setting
    for setting in settings:
        # get the algorithm from MAP (defined in presets.py)
        algorithm_class = algorithm_map[setting["name"]]
        if algorithm_class:
            # now get the params based on mode (low | high)
            params = setting["params"]
            setting_name += f"{setting['name']}#{setting['params']}-"
            if params:
                # finally we build our layered algorithm
                layers.append(algorithm_class(*params))

    # create our architecture
    target = Layers(raw_layers=layers, accuracy_calculator=accuracy_calculator)

    print(f"running permutation: {setting_name}")

    # TODO move time into layer
    start_time = time.perf_counter()
    target.run(dataset["paths"][:size])
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    # we want to get the groups of which the images belongs too
    preprocessed_results = target.group_related_images(target.result_duplicates)

    if accuracy_calculator:
        target.print_final_results(
            elapsed_time=elapsed_time,
            lonely_imgs=None,
            filename=os.path.join(current_script_dir, "outputs", foldername, f"{setting_name}.txt"),
        )

        with open(os.path.join(current_script_dir, "outputs", foldername, f"{setting_name}.json"), 'w') as file:
            json.dump({
                'duplicates': target.result_duplicates,
                'non-duplicates': target.result_possible_duplicates
            }, file)


# config = Array<{ name:string, params: Array<number> }>
def experiment(dataset, layer_size=3, dataset_size=-1, config="all", accuracy_calculator=None, presets={}, foldername=""):
    foldername=f"{foldername}-size={dataset_size}"
    output_path = os.path.join(current_script_dir, "outputs", foldername)
    if not os.path.exists(output_path):
        # If it doesn't exist, create it
        os.makedirs(output_path)

    if config == "all":
        config = []
        for algorithm_name in algorithm_map:
            if presets[algorithm_name]:
                config.append(
                    {
                        "name": algorithm_name,
                        "params": presets[algorithm_name],
                    }
                )
    perumation_sets = list(permutations(config, min(layer_size, len(config))))

    for setting in perumation_sets:
        test_permutation(
            settings=setting,
            foldername=foldername,
            dataset=dataset,
            size=dataset_size,
            accuracy_calculator=accuracy_calculator,
        )


def get_dataset(path):
    rootfolder = os.path.normpath(os.path.join(current_script_dir, ".."))
    filepath = os.path.join(rootfolder, "datasets", path)

    # Open the file and parse the JSON
    with open(filepath, "r") as file:
        data = json.load(file)

    # Update 'paths' with the rootfolder
    data['paths'] = [os.path.join(rootfolder, path) for path in data['paths']]

    # Update each string in 'groups'
    data['groups'] = [[os.path.join(rootfolder, path) for path in group] for group in data['groups']]

    # Update the keys in 'map' with the rootfolder
    data['map'] = {os.path.join(rootfolder, key): value for key, value in data['map'].items()}

    return data