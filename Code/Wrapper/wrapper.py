class Wrapper:
    """
    Wraps a given algorithm class with compatbility layer.
    Allows for running and getting/printing results.
    """

    def __init__(self, algorithm):
        self.algorithm = algorithm
        self.name = algorithm.name

    def run(self, image_paths):
        """
        Executes the given algorithm.
        """
        self.algorithm.process(image_paths)

        if isinstance(self.algorithm.duplicates, set):
            self.algorithm.duplicates = list(self.algorithm.duplicates)
            self.algorithm.non_duplicates = list(self.algorithm.non_duplicates)
            self.algorithm.possible_duplicates = list(
                self.algorithm.possible_duplicates
            )

    def get_results(self):
        """
        Returns resulting image path arrays.
        """
        return (
            self.algorithm.duplicates,
            self.algorithm.non_duplicates,
            self.algorithm.possible_duplicates,
        )

    def print_results(self):
        """
        Nicely formats and prints the resulting arrays of paths.
        """
        print("\nResults for", self.name)
        print("~~~~~~")
        print("Duplicates:")
        if self.algorithm.duplicates:
            for item in self.algorithm.duplicates:
                print(f"- {item}")
        else:
            print("- None")

        print("\nNon-Duplicates:")
        if self.algorithm.non_duplicates:
            for item in self.algorithm.non_duplicates:
                print(f"- {item}")
        else:
            print("- None")

        print("\nPossible Duplicates:")
        if self.algorithm.possible_duplicates:
            for item in self.algorithm.possible_duplicates:
                print(f"- {item}")
        else:
            print("- None")
