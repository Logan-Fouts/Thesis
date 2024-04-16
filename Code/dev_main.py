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


image_paths = get_image_paths("Images/Altered/Altered-Easy")
layers = [
    SIFT(threshold=20, image_ratio=1, sigma=1.7, edgeThreshold=1000**10, plot=False)
]

layered_architecure = Layers(layers)
layered_architecure.run(image_paths[:900])
layered_architecure.print_final_results()

# layered_architecure = Layers(layers)
# layered_architecure.run(image_paths[:900])
# layered_architecure.print_final_results()
