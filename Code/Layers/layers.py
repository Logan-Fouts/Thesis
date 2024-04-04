from Wrapper.wrapper import Wrapper


class Layers:
    """
    Builds and allows for execution of the layered architecure.
    """

    def __init__(self, raw_layers, debug=False):
        self.layers = []
        self.result_duplicates = set()
        self.debug = debug
        self.result_non_duplicates = set()
        self.result_possible_duplicates = set()
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
                if self.debug:
                    layer.print_results()
                tmp_duplicates, tmp_non_duplicates, tmp_possible_duplicates = (
                    layer.get_results()
                )

                self.result_duplicates.update(tmp_duplicates)
                self.result_non_duplicates.update(tmp_non_duplicates)
                self.result_possible_duplicates.update(tmp_possible_duplicates)
            else:
                print("Done")

    def print_final_results(self):
        """
        Nicely formats and prints the final resulting arrays of paths.
        """
        print("\nFINAL RESULTS...")
        print("~~~~~~")
        print("Duplicates:")
        if self.result_duplicates:
            for item in self.result_duplicates:
                print(f"- {item}")
        else:
            print("- None")
