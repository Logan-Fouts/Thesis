import random

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
            self.parent[item] = self.find(self.parent[item])
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
        self.acc_calc = accuracy_calculator
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
        curr_paths = set(image_paths)

        for layer in self.layers:
            if len(curr_paths) < 1:
                continue

            layer.run(curr_paths)
            tmp_dups, _ = layer.get_results()

            curr_paths = self._setup_further_processing(tmp_dups, curr_paths)

            if self.debug:
                layer.print_results()

        lst = [item for tup in self.result_duplicates for item in tup]
        self.result_possible_duplicates = list(set(curr_paths) - set(lst))

    def _setup_further_processing(self, duplicates, image_paths):
        """
        Clean up curr_paths and result_duplicates for further processing.
        """
        for duplicate_group in duplicates:
            if duplicate_group not in self.result_duplicates:
                self.result_duplicates.append(duplicate_group)

        lst = [item for tup in self.result_duplicates for item in tup]
        curr_paths = set(image_paths) - set(lst)

        self.result_duplicates = self.group_related_images(self.result_duplicates)

        # Grab a random image from each group and add to the current_image_paths to give further layers a chance
        for group in self.result_duplicates:
            if group:
                rand_img = random.choice(group)
                curr_paths.add(rand_img)

        return curr_paths

    def group_related_images(self, tuples):
        """
        Group all related duplicate image pairs into clusters.
        Assume that tuples might be a list of lists or list of tuples with more than two items.
        """
        uf = UnionFind()
        for group in tuples:
            if isinstance(group, (list, tuple)):
                for i in range(len(group) - 1):
                    for j in range(i + 1, len(group)):
                        uf.add(group[i])
                        uf.add(group[j])
                        uf.union(group[i], group[j])
            else:
                uf.add(group)
                uf.union(group, group)

        groups = {}
        for image in uf.parent:
            root = uf.find(image)
            if root not in groups:
                groups[root] = []
            groups[root].append(image)
        return list(groups.values())

    def calculate_metrics(self, tp, fp, tn, fn):
        """
        Calculate precision, recall, F1-score, and accuracy
        """
        precision = tp / (tp + fp) if tp + fp > 0 else 0
        recall = tp / (tp + fn) if tp + fn > 0 else 0
        f1_score = (
            2 * (precision * recall) / (precision + recall)
            if precision + recall > 0
            else 0
        )
        accuracy = (tp + tn) / (tp + fp + tn + fn) if tp + fp + tn + fn > 0 else 0

        return precision, recall, f1_score, accuracy

    def print_final_results(self, elapsed_time, filename="results.txt"):
        """
        Writes the final results to a file, formatting the output.
        """
        lst = [item for sub_lst in self.result_duplicates for item in sub_lst]

        print(
            "Final length of all results:",
            len(lst) + len(self.result_possible_duplicates),
        )

        self._write(filename, elapsed_time)

    def _write(self, filename, elapsed_time):
        with open(filename, "a", encoding="utf-8") as file:

            if not self.result_duplicates:
                return

            true_pos, false_pos, true_neg, false_neg = self.acc_calc(
                self.result_duplicates, self.result_possible_duplicates
            )
            precision, recall, f1_score, accuracy = self.calculate_metrics(
                true_pos, false_pos, true_neg, false_neg
            )

            result_text = (
                f"- TP: {true_pos}\n"
                f"- FP: {false_pos}\n"
                f"- TN: {true_neg}\n"
                f"- FN: {false_neg}\n\n"
            )
            result_metrics = (
                f"- Precision: {precision:.4f}\n"
                f"- Recall: {recall:.4f}\n"
                f"- F1-Score: {f1_score:.4f}\n"
                f"- Accuracy: {accuracy:.4f}\n"
            )

            total_images = true_pos + true_neg + false_pos + false_neg
            print(result_text)
            print(result_metrics)
            print(f"Total: {total_images}")
            print(f"Total Groups: {len(self.result_duplicates)}\n")

            file.write(f"\n## Num Images: {total_images}\n")
            file.write(result_text)
            file.write(result_metrics)
            file.write(f"Elapsed Time: {elapsed_time:.4f}\n\n")
            # for i, group in enumerate(related_groups, 1):
            #     file.write(f"Group {i}: {group}\n")
