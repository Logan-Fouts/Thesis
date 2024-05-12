import matplotlib.pyplot as plt
import pandas as pd

# Defining the number of images evaluated
image_counts = [300, 600, 900, 1200, 1500, 1800, 2100, 2400, 2700, 3000]

# Performance metrics from each method
# Dhash metrics
dhash_precision = [
    1.0000,
    0.9771,
    0.9538,
    0.9044,
    0.8388,
    0.8106,
    0.7707,
    0.7681,
    0.7467,
    0.7293,
]
dhash_recall = [
    0.7733,
    0.7963,
    0.7855,
    0.7764,
    0.7594,
    0.7518,
    0.7496,
    0.7496,
    0.7440,
    0.7321,
]
dhash_f1 = [
    0.8722,
    0.8775,
    0.8615,
    0.8355,
    0.7971,
    0.7801,
    0.7600,
    0.7587,
    0.7454,
    0.7307,
]
dhash_accuracy = [
    0.7733,
    0.7817,
    0.7567,
    0.7175,
    0.6627,
    0.6394,
    0.6129,
    0.6112,
    0.5941,
    0.5757,
]

# Phash metrics
phash_precision = [
    1.0000,
    0.9851,
    0.9310,
    0.9102,
    0.9034,
    0.8904,
    0.8590,
    0.8212,
    0.7904,
    0.7786,
]
phash_recall = [
    0.4533,
    0.4430,
    0.4489,
    0.4409,
    0.4441,
    0.4528,
    0.4484,
    0.4337,
    0.4226,
    0.4081,
]
phash_f1 = [
    0.6239,
    0.6111,
    0.6057,
    0.5940,
    0.5955,
    0.6003,
    0.5892,
    0.5676,
    0.5507,
    0.5355,
]
phash_accuracy = [
    0.4533,
    0.4400,
    0.4344,
    0.4225,
    0.4240,
    0.4289,
    0.4176,
    0.3962,
    0.3800,
    0.3657,
]

# SIFT metrics
sift_precision = [
    1.0000,
    1.0000,
    0.9933,
    0.9924,
    0.9886,
    0.9871,
    0.9818,
    0.9883,
    0.9889,
    0.9883,
]
sift_recall = [
    1.0000,
    1.0000,
    0.9944,
    0.9933,
    0.9919,
    0.9921,
    0.9922,
    0.9941,
    0.9970,
    0.9983,
]
sift_f1 = [
    1.0000,
    1.0000,
    0.9939,
    0.9929,
    0.9902,
    0.9896,
    0.9870,
    0.9912,
    0.9930,
    0.9933,
]
sift_accuracy = [
    1.0000,
    1.0000,
    0.9878,
    0.9858,
    0.9807,
    0.9794,
    0.9743,
    0.9825,
    0.9859,
    0.9867,
]

# Combined technique metrics (Phash, Dhash, SIFT)
combined_precision = [
    1.0000,
    1.0000,
    0.9921,
    0.9806,
    0.9682,
    0.9674,
    0.9643,
    0.9594,
    0.9541,
    0.9481,
]
combined_recall = [
    1.0000,
    0.9967,
    0.9888,
    0.9873,
    0.9862,
    0.9874,
    0.9867,
    0.9848,
    0.9833,
    0.9821,
]

combined_f1 = [
    1.0000,
    0.9983,
    0.9905,
    0.9839,
    0.9772,
    0.9773,
    0.9754,
    0.9719,
    0.9685,
    0.9648,
]
combined_accuracy = [
    1.0000,
    0.9967,
    0.9811,
    0.9683,
    0.9553,
    0.9556,
    0.9519,
    0.9454,
    0.9389,
    0.9320,
]

dhash_times = [
    0.5860,
    1.5984,
    3.4829,
    5.9875,
    9.1050,
    13.0436,
    17.7709,
    23.1121,
    28.8299,
    35.2138,
]
sift_times = [
    8.9167,
    35.1776,
    83.9491,
    203.7829,
    256.1593,
    405.4019,
    522.8061,
    674.3012,
    853.0779,
    1058.9478,
]
phash_times = [
    0.5607,
    1.6792,
    3.4975,
    6.1538,
    9.4956,
    13.5998,
    17.9561,
    23.7246,
    29.2554,
    35.6239,
]
combined_times = [
    2.5530,
    9.1599,
    19.7361,
    33.8846,
    51.8370,
    73.3654,
    98.9018,
    129.8883,
    154.1421,
    187.5546,
]

# Creating DataFrame
df = pd.DataFrame(
    {
        "Images": image_counts,
        "Dhash Precision": dhash_precision,
        "Dhash Recall": dhash_recall,
        "Dhash F1": dhash_f1,
        "Dhash Accuracy": dhash_accuracy,
        "Phash Precision": phash_precision,
        "Phash Recall": phash_recall,
        "Phash F1": phash_f1,
        "Phash Accuracy": phash_accuracy,
        "SIFT Precision": sift_precision,
        "SIFT Recall": sift_recall,
        "SIFT F1": sift_f1,
        "SIFT Accuracy": sift_accuracy,
        "Combined Precision": combined_precision,
        "Combined Recall": combined_recall,
        "Combined F1": combined_f1,
        "Combined Accuracy": combined_accuracy,
    }
)

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Precision
for column in [
    "Dhash Precision",
    "Phash Precision",
    "SIFT Precision",
    "Combined Precision",
]:
    axs[0, 0].plot(df["Images"], df[column], label=column.split()[0])
axs[0, 0].set_title("Precision by Number of Images")
axs[0, 0].set_xlabel("Number of Images")
axs[0, 0].set_ylabel("Precision")
axs[0, 0].legend()

# Recall
for column in ["Dhash Recall", "Phash Recall", "SIFT Recall", "Combined Recall"]:
    axs[0, 1].plot(df["Images"], df[column], label=column.split()[0])
axs[0, 1].set_title("Recall by Number of Images")
axs[0, 1].set_xlabel("Number of Images")
axs[0, 1].set_ylabel("Recall")
axs[0, 1].legend()

# F1-Score
for column in ["Dhash F1", "Phash F1", "SIFT F1", "Combined F1"]:
    axs[1, 0].plot(df["Images"], df[column], label=column.split()[0])
axs[1, 0].set_title("F1-Score by Number of Images")
axs[1, 0].set_xlabel("Number of Images")
axs[1, 0].set_ylabel("F1-Score")
axs[1, 0].legend()

# Accuracy
for column in [
    "Dhash Accuracy",
    "Phash Accuracy",
    "SIFT Accuracy",
    "Combined Accuracy",
]:
    axs[1, 1].plot(df["Images"], df[column], label=column.split()[0])
axs[1, 1].set_title("Accuracy by Number of Images")
axs[1, 1].set_xlabel("Number of Images")
axs[1, 1].set_ylabel("Accuracy")
axs[1, 1].legend()

plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))

plt.plot(image_counts, dhash_times, marker="o", color="blue", label="Dhash")
plt.plot(image_counts, sift_times, marker="o", color="red", label="SIFT")
plt.plot(image_counts, phash_times, marker="o", color="green", label="Phash")
plt.plot(image_counts, combined_times, marker="o", color="purple", label="Combined")

plt.title("Time Elapsed for Image Processing Algorithms")
plt.xlabel("Number of Images")
plt.ylabel("Time Elapsed (seconds)")
plt.legend()
plt.grid(True)
plt.show()
