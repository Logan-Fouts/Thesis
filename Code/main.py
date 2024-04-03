from Dhash.dhash import Dhash
from Layers.layers import Layers
from VGG.vgg import VGG
from Wrapper.wrapper import Wrapper

image_paths = [
    "Images/image8.png",
    "Images/image9.png",
]
layers = [Dhash(), VGG()]
layered_architecure = Layers(layers)
layered_architecure.run(image_paths)
