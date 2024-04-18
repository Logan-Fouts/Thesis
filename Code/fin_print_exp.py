import os
import random
import sys
import time
from collections import defaultdict

from cv2 import threshold

project_root = os.path.dirname(os.path.abspath(__file__))
algorithms_path = os.path.join(project_root, "Algorithms")
integration_path = os.path.join(project_root, "Integration")

sys.path.append(algorithms_path)
sys.path.append(integration_path)

from Ahash.ahash import Ahash
from Dhash.dhash import Dhash
from Layers.layers import Layers
from MinHash_LSH.minhash_lsh import MinHash_LSH
from Phash.phash import Phash
from SIFT.sift import SIFT
from SSIM.ssim import SSIM
from VGG.vgg import VGG


def get_image_paths(directory):
    """
    Recursively grabs image paths from directory and stores in an array.
    """
    paths = []
    extensions = {".jpg", ".jpeg", ".png", ".bmp"}

    for root, _, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1].lower() in extensions:
                paths.append(os.path.join(root, file))

    paths.sort()
    return paths


def group_images(paths):
    grouped_paths = defaultdict(list)
    for path in paths:
        filename = os.path.basename(path)
        parts = filename.split("_")
        group_key = "_".join(parts[:5])
        grouped_paths[group_key].append(path)

    return grouped_paths


def finger_accuracy_calculator(duplicate_pairs):
    """
    Default method to calculate the accuracy of duplicate detection.
    """
    correct = 0
    total = len(duplicate_pairs)

    for path1, path2 in duplicate_pairs:
        parts1 = path1.split("/")[-1].split("_")
        parts2 = path2.split("/")[-1].split("_")

        num1 = parts1[0]
        num2 = parts2[0]

        finger1 = "_".join(parts1[2:5]) if len(parts1) > 4 else ""
        finger2 = "_".join(parts2[2:5]) if len(parts2) > 4 else ""

        if num1 == num2 and finger1 == finger2:
            correct += 1

    return (correct / total) * 100 if total > 0 else 0


SZ = 1800
image_paths = get_image_paths("Images/Finger_Prints/Altered/Altered-Easy")
groups = group_images(image_paths[:SZ])
test_paths = []
for group in groups.values():
    test_paths.extend(group)
print(len(groups))
layers = [
    Phash(threshold=4),
    Dhash(threshold=3),
    SIFT(
        threshold=17,
        sigma=1.8,
        edge_threshold=1000 * 10,
        n_octave_layers=3,
        contrast_threshold=0.01,
        plot=False,
    ),
    # Not sure if we should keep ssim here or not.
    SSIM(threshold=0.95),
]
layered_architecure = Layers(
    raw_layers=layers, accuracy_calculator=finger_accuracy_calculator
)
start_time = time.perf_counter()
layered_architecure.run(test_paths)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
layered_architecure.print_final_results()
print(f"Elapsed time: {elapsed_time:.4f} seconds")
