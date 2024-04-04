from itertools import combinations

import cv2


class SIFT:
    """
    Uses open cv to implement SIFT.
    """

    def __init__(self, threshold=40, error=15, image_ratio=0.25, plot=False):
        self.name = "SIFT"
        self.threshold = threshold
        self.error = error
        self.image_ratio = image_ratio
        self.plot = plot
        self.duplicates = set()
        self.non_duplicates = set()
        self.possible_duplicates = set()

    def process(self, image_paths):
        """
        Uses sift to classify images.
        """
        preprocessed_images = self._preprocess(image_paths)

        for path1, path2 in combinations(preprocessed_images.keys(), 2):
            _, _, descriptors1 = preprocessed_images[path1]
            _, _, descriptors2 = preprocessed_images[path2]

            if descriptors1 is None or descriptors2 is None:
                print(f"Descriptors missing for images: {path1} or {path2}")
                continue

            matches = cv2.BFMatcher().knnMatch(descriptors1, descriptors2, k=2)

            close_enough_matches = self._calc_lowe(matches)

            if self.plot:
                self._plot(
                    close_enough_matches,
                    preprocessed_images[path1],
                    preprocessed_images[path2],
                )

            result = self._filter(close_enough_matches)
            if result == 0:
                self.duplicates.update((path1, path2))
            elif result == 1:
                self.possible_duplicates.update((path1, path2))
            else:
                self.non_duplicates.update((path1, path2))

    def _preprocess(self, image_paths):
        preprocessed_images = {}
        for path in image_paths:
            img = cv2.imread(path)
            if img is None:  # Check if the image was not loaded successfully
                print(f"Failed to open image: {path}.")
                continue  # Skip this image and proceed with the next one
            image = cv2.resize(img, None, fx=self.image_ratio, fy=self.image_ratio)
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            sift = cv2.SIFT_create()
            keypoints, descriptors = sift.detectAndCompute(gray_image, None)
            preprocessed_images[path] = (gray_image, keypoints, descriptors)
        return preprocessed_images

    def _calc_lowe(self, matches):
        close_enough_matches = []
        for m, n in matches:
            if m.distance < 0.75 * n.distance:
                close_enough_matches.append(m)
        return close_enough_matches

    def _plot(self, matches, oim1, oim2):
        import matplotlib.pyplot as plt

        im1, kp1, _ = oim1
        im2, kp2, _ = oim2

        num_matches = min(200, len(matches))
        match_img = cv2.drawMatches(
            im1,
            kp1,
            im2,
            kp2,
            matches[:num_matches],
            None,
        )
        plt.figure(figsize=(12, 6))
        plt.imshow(match_img)
        plt.show()

    # TODO: Move filter into a new class or something.

    def _filter(self, matches):
        """
        Determine category based on the number of matches.
        """
        if len(matches) > self.threshold:
            return 0
        if len(matches) > self.threshold - self.error:
            return 1
        return 2
