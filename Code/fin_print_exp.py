import os
import sys
import time
from collections import defaultdict

# Make python see the modules by adding paths to the path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(project_root, "Algorithms"))
sys.path.append(os.path.join(project_root, "Integration"))

# Import modules
from Dhash.dhash import Dhash
from Layers.layers import Layers
from Phash.phash import Phash
from SIFT.sift import SIFT
from SSIM.ssim import SSIM


def get_image_paths(directory):
    """
    Recursively grabs image paths from directory and stores in an array.
    """
    extensions = {".jpg", ".jpeg", ".png", ".bmp"}
    paths = [
        os.path.join(root, file)
        for root, _, files in os.walk(directory)
        for file in files
        if os.path.splitext(file)[1].lower() in extensions
    ]
    paths.sort()
    return paths


def group_images(paths):
    """
    Groups image paths based on the file names since the data set is a little weird.
    """
    grouped_paths = defaultdict(list)
    for path in paths:
        group_key = "_".join(os.path.basename(path).split("_")[:5])
        grouped_paths[group_key].append(path)
    return grouped_paths


def finger_accuracy_calculator(duplicate_pairs):
    """
    Calculates the accuracy for the images classified as duplicates.
    """
    correct = sum(
        path1.split("/")[-1].split("_")[0] == path2.split("/")[-1].split("_")[0]
        and "_".join(path1.split("/")[-1].split("_")[2:5])
        == "_".join(path2.split("/")[-1].split("_")[2:5])
        for path1, path2 in duplicate_pairs
    )
    total = len(duplicate_pairs)
    return (correct / total) * 100 if total > 0 else 0


def run_experiment(size, path):
    # Config for Finger Prints Dataset
    SZ = size
    image_paths = get_image_paths(path)
    groups = group_images(image_paths[:SZ])
    test_paths = [path for group in groups.values() for path in group]

    print(f"Number of groups: {len(groups)}")

    layers = [
        Phash(threshold=4),
        Dhash(threshold=3),
        SIFT(
            threshold=17,
            sigma=1.8,
            edge_threshold=10000,
            n_octave_layers=3,
            contrast_threshold=0.01,
            plot=False,
        ),
        # SSIM(threshold=0.95),  # Not sure if we should keep ssim here or not.
    ]

    layered_architecture = Layers(
        raw_layers=layers, accuracy_calculator=finger_accuracy_calculator
    )

    # Measure execution time
    start_time = time.perf_counter()
    layered_architecture.run(test_paths)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    layered_architecture.print_final_results(time_elapsed=elapsed_time, size=SZ)
    print(f"Elapsed time: {elapsed_time:.4f} seconds")


for i in range(300, 3300, 300):
    run_experiment(i, "Images/Finger_Prints/Altered/Altered-Easy")
