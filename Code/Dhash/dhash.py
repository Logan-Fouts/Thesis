import imagehash
from PIL import Image


class Dhash:
    def __init__(self, threshold=20, error=10):
        self.name = "Dhash"
        self.threshold = threshold
        self.error = error
        self.duplicates = []
        self.non_duplicates = []
        self.possible_duplicates = []

    def process(self, image_paths):
        """
        Takes provided image paths and classifies them as duplicates, not duplicates, or unsure.
        """
        hashes = {image_path: self._dhash(image_path) for image_path in image_paths}
        checked_pairs = set()

        for path1, hash1 in hashes.items():
            for path2, hash2 in hashes.items():
                if path1 >= path2 or (path1, path2) in checked_pairs:
                    continue

                result = self._filter(hash1, hash2)

                if result == 0:
                    if path1 not in self.duplicates:
                        self.duplicates.append(path1)
                    if path2 not in self.duplicates:
                        self.duplicates.append(path2)
                elif result == 1:
                    if path1 not in self.possible_duplicates:
                        self.possible_duplicates.append(path1)
                    if path2 not in self.possible_duplicates:
                        self.possible_duplicates.append(path2)
                elif result == 2:
                    if path1 not in self.non_duplicates:
                        self.non_duplicates.append(path1)
                    if path2 not in self.non_duplicates:
                        self.non_duplicates.append(path2)

                checked_pairs.add((path1, path2))
        self.non_duplicates = [
            path for path in self.non_duplicates if path not in self.possible_duplicates
        ]

    def _dhash(self, image_path):
        image = Image.open(image_path)
        return imagehash.dhash(image)

    def _filter(self, h1, h2):
        """
        Uses hamming distance to classify images.
        0 = duplicates, 1 = possible duplicates, 2 = not duplicates
        """
        hamming_distance = abs(h1 - h2)
        if hamming_distance <= self.threshold:
            return 0
        if self.threshold < hamming_distance < self.threshold + self.error:
            return 1
        else:
            return 2
