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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find duplicate images.")
    parser.add_argument(
        "folder_path", type=str, help="Path to the folder containing images."
    )
    parser.add_argument(
        "-l",
        "--layers",
        nargs="+",
        help="List of layers to use in order (e.g., Phash Dhash VGG SIFT)",
        default=[],
    )
    args = parser.parse_args()
    main(args.folder_path, args.layers)
