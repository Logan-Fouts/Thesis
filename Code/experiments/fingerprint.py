import permutation

# accuracy caculaters
def accuracy_calculator(duplicate_pairs):
  # Calculates the accuracy for the images classified as duplicates.
  correct = sum(
    path1.split("/")[-1].split("_")[0] == path2.split("/")[-1].split("_")[0]
    and "_".join(path1.split("/")[-1].split("_")[2:5])
    == "_".join(path2.split("/")[-1].split("_")[2:5])
    for path1, path2 in duplicate_pairs
  )

  total = len(duplicate_pairs)
  return (correct / total) * 100 if total > 0 else 0

print("running fingerprint experiment")

permutation.compare(
  dataset=permutation.get_dataset("datasets/fingerprint/output.json"), 
  dataset_size=90, 
  accuracy_calculator=accuracy_calculator,
  preset=permutation.preset['fingerprint']
)