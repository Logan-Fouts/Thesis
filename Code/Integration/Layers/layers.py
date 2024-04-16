from Wrapper.wrapper import Wrapper


class UnionFind:
    """A simple Union-Find class to manage merging of related groups."""

    def __init__(self):
        self.parent = {}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, item1, item2):
        root1 = self.find(item1)
        root2 = self.find(item2)
        if root1 != root2:
            self.parent[root2] = root1

    def add(self, item):
        if item not in self.parent:
            self.parent[item] = item


class Layers:
    """
    Builds and allows for execution of the layered architecure.
    """

    def __init__(self, raw_layers, debug=False):
        self.layers = []
        self.debug = debug
        self.result_duplicates = []
        self.result_possible_duplicates = []
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
        current_image_paths = set(image_paths)
        for layer in self.layers:
            if len(current_image_paths) > 1:
                layer.run(current_image_paths)
                tmp_duplicates, tmp_possible_duplicates = layer.get_results()
                if self.debug:
                    layer.print_results()

                self.result_duplicates.extend(tmp_duplicates)
                self.result_possible_duplicates.extend(tmp_possible_duplicates)

                current_image_paths = set(tmp_possible_duplicates)
            else:
                print("Done Early!")

    def calculate_accuracy(self, duplicate_pairs):
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

        accuracy = (correct / total) * 100 if total > 0 else 0
        return accuracy

    def group_related_images(self):
        """Group all related duplicate image pairs into clusters."""
        uf = UnionFind()
        for path1, path2 in self.result_duplicates:
            uf.add(path1)
            uf.add(path2)
            uf.union(path1, path2)

        groups = {}
        for image in uf.parent:
            root = uf.find(image)
            if root not in groups:
                groups[root] = []
            groups[root].append(image)
        return list(groups.values())

    def print_final_results(self, filename="results.txt"):
        """
        Writes the final results to a file, formatting the output.
        """
        related_groups = self.group_related_images()
        with open(filename, "w") as file:
            file.write("\nFINAL RESULTS...\n")
            file.write("~~~~~~\n")

            if self.result_duplicates:
                accuracy = self.calculate_accuracy(self.result_duplicates)
                file.write(f"Accuracy: {accuracy:.2f}%\n")
                print(f"Accuracy: {accuracy:.2f}%\n")

            file.write(f"Total Groups: {len(related_groups)}\n")
            print(f"Total Groups: {len(related_groups)}\n")
            for i, group in enumerate(related_groups, 1):
                file.write(f"Group {i}: {group}\n")
