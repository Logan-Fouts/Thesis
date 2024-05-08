import permutation
from collections import Counter

# accuracy caculaters
def accuracy_calculator(duplicate_groups, non_duplicate_list, lonely_imgs):
    """
    Method to calculate the accuracy of duplicate detection.
    """
    true_pos = 0
    false_pos = 0
    true_neg = 0

    if lonely_imgs:
        for img in non_duplicate_list:
            if img in lonely_imgs:
                true_neg += 1

    false_neg = len(non_duplicate_list) - true_neg

    for dup_group in duplicate_groups:
        relevant_parts = [item.split("/")[-1].split("_")[0:5] for item in dup_group]
        relevant_parts_combined = ["_".join(parts) for parts in relevant_parts]
        most_common_segment, _ = Counter(relevant_parts_combined).most_common(1)[0]

        for path in dup_group:
            relevant_part = "_".join(path.split("/")[-1].split("_")[:5])
            match = most_common_segment == relevant_part

            if match:
                true_pos += 1
            else:
                false_pos += 1

    return true_pos, false_pos, true_neg, false_neg
    
print("running fingerprint experiment")

permutation.experiment(
  dataset=permutation.get_dataset("fingerprint/output.json"), 
  dataset_size=10, 
  accuracy_calculator=accuracy_calculator,
  presets=permutation.presets['fingerprint'],
  foldername="fingerprint-easy"
)
