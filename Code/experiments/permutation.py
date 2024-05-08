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
# from VGG.vgg import VGG

# Open the file and load the data
with open('presets.json', 'r') as file:
    presets = json.load(file)

# algorithm_map = {"dhash": Dhash, "phash": Phash, "sift": SIFT, "vgg": VGG}
algorithm_map = {"dhash": Dhash, "phash": Phash, "sift": SIFT}

# helper functions
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
    layered_architecture = Layers(
        raw_layers=layers, accuracy_calculator=accuracy_calculator
    )

    # TODO move time into layer
    start_time = time.perf_counter()
    layered_architecture.run(dataset["paths"][:size])
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    # we want to get the groups of which the images belongs too (as )
    # preprocessed_results = preprocess_results(layered_architecture)
    preprocessed_results = layered_architecture.group_related_images(layered_architecture.result_duplicates)

    if accuracy_calculator:
        layered_architecture.print_final_results(
            elapsed_time=elapsed_time,
            lonely_imgs=None,
            filename=os.path.join(current_script_dir, "outputs", foldername, f"{setting_name}.txt"),
        )
    else:
        true_positives = 0
        false_positives = 0

        for group in preprocessed_results:
            if len(group) > 0:
                compare_map = {}

                for path in group:
                    if dataset["map"][path] not in compare_map:
                        compare_map[dataset["map"][path]] = 0

                    compare_map[dataset["map"][path]] += 1

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
def experiment(dataset, layer_size=3, dataset_size=-1, config="all", accuracy_calculator=None, presets={}, foldername=""):
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
                # for mode in presets[algorithm_name]:
                #     config.append(
                #         {
                #             "name": algorithm_name,
                #             "params": presets[algorithm_name][mode],
                #         }
                #     )

    perumation_sets = list(permutations(config, layer_size))

    # tp, fp = test_permutation(settings=[{'name': "phash", 'params': [4]}, {'name': 'dhash', 'params': [3]}, {'name': 'sift', 'params': [17, 1.8, 10000, 3, 0.01]}], dataset=dataset, size=dataset_size, accuracy_calculator=accuracy_calculator)
    # print(f"# experiment finished ✅\nTP: {tp}, FP: {fp}")

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

