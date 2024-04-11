import re
import utils

def generate_shingles(text, K, verbose=False):
    # Split the text into words using regular expressions
    words = re.findall(r'\w+', text.lower())  # \w+ matches alphanumeric characters

    shingles_hashes = []
    for i in range(len(words) - K + 1):
        # Create a shingle by joining K consecutive words
        shingle = ' '.join(words[i:i+K])
        shingle_hash = utils.fnv1a_hash(shingle)
        shingles_hashes.append(shingle_hash)

        if verbose:
            print(f"Hash: {shingle_hash}, Shingle: {shingle}")

    return shingles_hashes

def generate_signatures(shingles):


# === TESTs =====
def test_generate_shingles():
    # Example usage
    K = 3  # Length of shingle in words
    text = "This is an example text with several words for processing."
    print("test_generate_shingles: \"", text, "\"\n")
    shingles = generate_shingles(text, K, True)

    print("\noutput:",shingles)