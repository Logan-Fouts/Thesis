from Dhash.dhash import Dhash
from Wrapper.wrapper import Wrapper


class Layers:
    """
    Builds and allows for execution of the layered architecure.
    """

    def __init__(self, raw_layers):
        self.layers = []
        self._wrap_layers(raw_layers)

    def _wrap_layers(self, raw_layers):
        """
        Wraps each given layer with a compatibility layer.
        """
        for layer in raw_layers:
            self.layers.append(Wrapper(layer))

    def get_wrapped_layers(self):
        """
        Returns an array of the wrapped layers.
        """
        return self.layers

    def run(self, image_paths):
        """
        Executes the classes given in sequence.
        """
        current_image_paths = image_paths
        for layer in self.layers:
            if len(image_paths) > 0:
                layer.run(current_image_paths)
                _, _, current_image_paths = layer.get_results()
                layer.print_results()
            else:
                print("Done")
