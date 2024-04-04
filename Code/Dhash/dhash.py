import imagehash
from PIL import Image, ImageFilter


class Dhash:
    def __init__(self, threshold=15, error=10):
        self.name = "Dhash"
        self.threshold = threshold
        self.error = error
        self.duplicates = set()
        self.non_duplicates = set()
        self.possible_duplicates = set()

    def process(self, image_paths):
        """
        Takes provided image paths and classifies them as duplicates, not duplicates, or unsure.
        """
        image_paths = set(image_paths)

        hashes = {image_path: self._dhash(image_path) for image_path in image_paths}
        checked_pairs = set()

        for path1, hash1 in hashes.items():
            for path2, hash2 in hashes.items():
                if (
                    path1 == path2
                    or (path1, path2) in checked_pairs
                    or (path2, path1) in checked_pairs
                ):
                    continue

                result = self._filter(hash1, hash2)
                pair = {path1, path2}

                if result == 0:
                    self.duplicates.update(pair)
                elif result == 1:
                    self.possible_duplicates.update(pair)
                elif result == 2:
                    self.non_duplicates.update(pair)

                checked_pairs.add((path1, path2))
                checked_pairs.add((path2, path1))

        # Remove any duplication
        # self.non_duplicates -= self.possible_duplicates
        # self.non_duplicates -= self.duplicates
        #
        # self.possible_duplicates -= self.non_duplicates
        # self.possible_duplicates -= self.duplicates
        #
        # self.duplicates -= self.possible_duplicates
        # self.duplicates -= self.non_duplicates

    def _dhash(self, image_path):
        try:
            with Image.open(image_path) as image:
                image = image.convert("L")
                image = image.resize((20, 20), Image.LANCZOS)
                image = image.filter(ImageFilter.BLUR)
                image = image.filter(ImageFilter.FIND_EDGES)
                return imagehash.dhash(image)
        except IOError as e:
            print(f"Error accessing image: {image_path}: {e}")
            return None

    def _filter(self, h1, h2):
        """
        Uses hamming distance to classify images.
        0 = duplicates, 1 = possible duplicates, 2 = not duplicates
        """
        hamming_distance = h1 - h2
        print(hamming_distance)
        if hamming_distance <= self.threshold:
            return 0
        if self.threshold < hamming_distance < self.threshold + self.error:
            return 1
        return 2
