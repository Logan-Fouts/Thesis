import imagehash
import numpy as np
from datasketch import MinHash, MinHashLSH
from PIL import Image


class MinHash_LSH:
    def __init__(self, num_perm=128, threshold=0.75):
        self.name = "MinHash LSH"
        self.lsh = MinHashLSH(threshold=threshold, num_perm=num_perm)
        self.num_perm = num_perm
        self.threshold = threshold
        self.duplicates = []
        self.possible_duplicates = []

    def process(self, image_paths):
        minhashes = {}

        for path in image_paths:
            image = Image.open(path)
            im_hash = imagehash.phash(image, hash_size=64)
            m = MinHash(num_perm=self.num_perm)

            for bit in np.nditer(im_hash.hash):
                m.update(bit.tobytes())

            minhashes[path] = m
            self.lsh.insert(path, m)

        # TODO: Cant really get this to work
        for path, minhash in minhashes.items():
            results = self.lsh.query(minhash)
            if len(results) > 1:
                for other_path in results:
                    if other_path != path:
                        jaccard_sim = minhash.jaccard(minhashes[other_path])
                        if jaccard_sim != 1.0:
                            print(jaccard_sim)
                        if jaccard_sim >= self.threshold:
                            self.duplicates.append((path, other_path))
                        else:
                            self.possible_duplicates.append((path, other_path))
