def fnv1a_hash(str_input):
  # FNV-1a constants
  hash_ = 2166136261
  prime = 16777619

  # Encode the string as UTF-16LE to get the byte representation
  # Python's 'utf-16le' encoding does not include the Byte Order Mark (BOM), making it suitable for hashing
  bytes_input = str_input.encode('utf-16le')

  # Iterate through each byte
  for byte in bytes_input:
      hash_ = hash_ ^ byte
      hash_ = (hash_ * prime) & 0xFFFFFFFF  # Ensure hash stays within 32-bit bounds

  return hash_


def test_fnv1a_hash():
  # Example usage
  my_string = "hello world"
  hash_value = fnv1a_hash(my_string)
  print(f"The FNV-1a hash of '{my_string}' is: {hash_value}")

