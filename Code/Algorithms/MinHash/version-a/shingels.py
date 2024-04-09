import re

def generate_shingles(text, K):
    # Split the text into words using regular expressions
    words = re.findall(r'\w+', text.lower())  # \w+ matches alphanumeric characters

    # Initialize the pipeline with the hash of the first K words, if available
    pipeline = [fnv1a_hash(word.encode('utf-8')) for word in words[:K]]

    # Process shingles and compute their hashes
    for i in range(len(words) - K + 1):
        # The current shingle is words[i:i+K]
        # Compute the hash for the current shingle if not already done
        if i != 0:
            new_word_hash = fnv1a_hash(words[i+K-1].encode('utf-8'))
            # Shift the pipeline and add the new word's hash
            pipeline = pipeline[1:] + [new_word_hash]
        
        # Collect or process the hash of the current shingle
        # For demonstration, we'll just print the hash and the corresponding shingle
        print(f"Hash: {pipeline[0]}, Shingle: {' '.join(words[i:i+K])}")

def main():
    # Example usage
    K = 3  # Length of shingle in words
    text = "This is an example text with several words for processing."
    generate_shingles(text, K)
