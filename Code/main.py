import os

from Dhash.dhash import Dhash
from Layers.layers import Layers
from SIFT.sift import SIFT
from VGG.vgg import VGG
from Wrapper.wrapper import Wrapper


def get_image_paths(directory):
    """
    Recursively grabs image paths from directory and stores in an array.
    """
    paths = []
    valid_extensions = {".jpg", ".jpeg", ".png"}

    for root, _, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1].lower() in valid_extensions:
                paths.append(os.path.join(root, file))

    return paths


image_paths = get_image_paths("Images/Manual_Tests")
layers = [Dhash(), VGG(), SIFT()]
layered_architecure = Layers(layers, debug=True)
layered_architecure.run(image_paths)
layered_architecure.print_final_results()
