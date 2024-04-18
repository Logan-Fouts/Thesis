from Wrapper.wrapper import Wrapper


class UnionFind:
    """
    A simple Union-Find class to manage a collection of disjoint sets.
    """

    def __init__(self):
        """
        Initializes the Union-Find structure.
        """
        self.parent = {}

    def find(self, item):
        """
        Finds and returns the root of the set containing the item and does path compression.
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])  # Path compression
        return self.parent[item]

    def union(self, item1, item2):
        """
        Merges the sets that have item1 and item2. Uses rank.
        """
        root1 = self.find(item1)
        root2 = self.find(item2)
        if root1 != root2:
            self.parent[root2] = root1

    def add(self, item):
        """
        Adds an item.
        """
        if item not in self.parent:
            self.parent[item] = item


class Layers:
    """
    Builds and allows for execution of the layered architecture.
    """

    def __init__(self, raw_layers, accuracy_calculator=None, debug=False):
        self.layers = []
        self._wrap_layers(raw_layers)
        self.accuracy_calculator = accuracy_calculator
        self.debug = debug
        self.result_duplicates = []
        self.result_possible_duplicates = []

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

                duplicates_set = set(path for dup in tmp_duplicates for path in dup)

                # Filter current_image_paths to exclude paths found in duplicates
                current_image_paths = set(tmp_possible_duplicates) - duplicates_set

                print(len(current_image_paths))
                import time

                time.sleep(1)
            else:
                print("Done Early!")

    def group_related_images(self):
        """
        Group all related duplicate image pairs into clusters.
        """
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
        print(related_groups)
        with open(filename, "w") as file:
            file.write("\nFINAL RESULTS...\n")
            file.write("~~~~~~\n")

            if self.result_duplicates:
                accuracy = self.accuracy_calculator(self.result_duplicates)
                file.write(f"Accuracy: {accuracy:.2f}%\n")
                print(f"Accuracy: {accuracy:.2f}%\n")

            file.write(f"Total Groups: {len(related_groups)}\n")
            print(f"Total Groups: {len(related_groups)}\n")
            for i, group in enumerate(related_groups, 1):
                file.write(f"Group {i}: {group}\n")
