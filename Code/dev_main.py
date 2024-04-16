import os
import sys

from cv2 import threshold

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
    extensions = {".jpg", ".jpeg", ".png", ".bmp"}

    for root, _, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1].lower() in extensions:
                paths.append(os.path.join(root, file))

    paths.sort()  # Make it repeatable
    return paths


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


image_paths = get_image_paths("Images/Altered/Altered-Easy")
layers = [
    SIFT(threshold=20, image_ratio=1, sigma=1.7, edgeThreshold=1000**10, plot=False)
]

layered_architecure = Layers(
    raw_layers=layers, accuracy_calculator=finger_accuracy_calculator
)
layered_architecure.run(image_paths[:900])
layered_architecure.print_final_results()
