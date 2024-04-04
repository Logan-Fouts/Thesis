import cv2


class SIFT:
    """
    Uses open cv to implement SIFT.
    """

    def __init__(self, threshold=40, error=15):
        self.name = "SIFT"
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

        for i, path1 in enumerate(image_paths):
            for path2 in list(image_paths)[i + 1 :]:
                image1, image2 = cv2.imread(path1), cv2.imread(path2)

                if image1 is None or image2 is None:
                    print(f"Failed to load images: {path1} or {path2}.")
                    continue

                image1 = cv2.resize(image1, None, fx=0.5, fy=0.5)
                image2 = cv2.resize(image2, None, fx=0.5, fy=0.5)

                gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
                gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

                sift = cv2.SIFT_create()

                _, descriptors1 = sift.detectAndCompute(gray1, None)
                _, descriptors2 = sift.detectAndCompute(gray2, None)

                matches = cv2.BFMatcher().knnMatch(descriptors1, descriptors2, k=2)

                result = self._filter(matches)

                pair = (path1, path2)
                if result == 0:
                    self.duplicates.update(pair)
                elif result == 1:
                    self.possible_duplicates.update(pair)
                elif result == 2:
                    self.non_duplicates.update(pair)

        self.non_duplicates -= self.possible_duplicates
        self.non_duplicates -= self.duplicates

        self.possible_duplicates -= self.non_duplicates
        self.possible_duplicates -= self.duplicates

        self.duplicates -= self.possible_duplicates
        self.duplicates -= self.non_duplicates

    def _filter(self, matches):
        close_matches = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                close_matches.append(m)

        if len(close_matches) > self.threshold:
            return 0
        if len(close_matches) > self.threshold - self.error:
            return 1
        return 2
