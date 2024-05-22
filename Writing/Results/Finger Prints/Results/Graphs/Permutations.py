import matplotlib.pyplot as plt
import numpy as np

# Data from the table
algorithms = [
    "Phash, SIFT, VGG",
    "Phash, SIFT, Dhash",
    "Phash, Dhash, VGG",
    "Phash, Dhash, SIFT",
    "Dhash, VGG, SIFT",
    "Dhash, VGG, Phash",
    "Dhash, SIFT, VGG",
    "Dhash, SIFT, Phash",
    "Dhash, Phash, VGG",
    "Dhash, Phash, SIFT",
    "Phash, VGG, Dhash",
    "Phash, VGG, SIFT",
    "SIFT, Dhash, Phash",
    "SIFT, Dhash, VGG",
    "SIFT, Phash, Dhash",
    "SIFT, Phash, VGG",
    "SIFT, VGG, Dhash",
    "SIFT, VGG, Phash",
    "VGG, Dhash, Phash",
    "VGG, Dhash, SIFT",
    "VGG, Phash, Dhash",
    "VGG, Phash, SIFT",
    "VGG, SIFT, Dhash",
    "VGG, SIFT, Phash",
]
time_elapsed = [
    4.67,
    3.19,
    8.53,
    3.18,
    9.00,
    9.11,
    4.90,
    3.25,
    8.21,
    3.22,
    8.90,
    8.98,
    3.26,
    4.35,
    3.26,
    4.18,
    4.34,
    4.30,
    8.62,
    8.88,
    8.79,
    8.64,
    8.78,
    8.68,
]
accuracy = [
    90.41,
    100.00,
    48.89,
    100.00,
    35.71,
    35.71,
    87.84,
    100.00,
    48.53,
    100.00,
    39.36,
    39.36,
    100.00,
    96.34,
    100.00,
    98.72,
    96.34,
    96.34,
    23.99,
    23.99,
    23.99,
    23.99,
    23.99,
    23.99,
]
group_numbers = [
    30,
    28,
    17,
    28,
    13,
    13,
    29,
    28,
    17,
    28,
    13,
    13,
    28,
    30,
    28,
    31,
    30,
    30,
    6,
    6,
    6,
    6,
    6,
    6,
]

x = np.arange(len(algorithms))

fig, ax1 = plt.subplots(figsize=(14, 8))

color = "blue"
ax1.set_xlabel("Algorithms Combination", fontsize=20)
ax1.set_ylabel("Time Elapsed (s)", color=color, fontsize=20)
ax1.bar(x, time_elapsed, color=color, label="Time Elapsed (s)")
ax1.tick_params(axis="y", labelcolor=color, labelsize=20)
ax1.tick_params(axis="x", rotation=90, labelsize=20)

ax2 = ax1.twinx()
color = "red"
ax2.set_ylabel("Accuracy (%)", color=color, fontsize=20)
ax2.plot(x, accuracy, color=color, marker="o", label="Accuracy (%)")
ax2.tick_params(axis="y", labelcolor=color, labelsize=20)
ax2.tick_params(axis="x", labelsize=20)

ax3 = ax1.twinx()
color = "green"
ax3.spines["right"].set_position(("outward", 60))
ax3.set_ylabel("Group Numbers", color=color, fontsize=20)
ax3.plot(x, group_numbers, color=color, marker="s", label="Group Numbers")
ax3.tick_params(axis="y", labelcolor=color, labelsize=20)
ax3.tick_params(axis="x", labelsize=18)

fig.tight_layout()
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9), fontsize=20)
plt.show()
