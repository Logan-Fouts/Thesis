import matplotlib.pyplot as plt
import numpy as np

# Sample data (Replace these with actual data from your graph)
time_elapsed = [
    100,
    150,
    200,
    300,
    700,
    800,
    500,
    300,
    250,
    400,
    450,
    350,
    250,
    200,
    150,
    100,
    50,
    25,
    30,
    40,
    60,
    80,
    100,
    120,
]
precision = [
    0.98,
    0.97,
    0.96,
    0.95,
    0.94,
    0.93,
    0.92,
    0.91,
    0.90,
    0.89,
    0.88,
    0.87,
    0.86,
    0.85,
    0.84,
    0.83,
    0.82,
    0.81,
    0.80,
    0.79,
    0.78,
    0.77,
    0.76,
    0.75,
]
recall = [
    0.95,
    0.94,
    0.93,
    0.92,
    0.91,
    0.90,
    0.89,
    0.88,
    0.87,
    0.86,
    0.85,
    0.84,
    0.83,
    0.82,
    0.81,
    0.80,
    0.79,
    0.78,
    0.77,
    0.76,
    0.75,
    0.74,
    0.73,
    0.72,
]
f1_score = [
    0.96,
    0.95,
    0.94,
    0.93,
    0.92,
    0.91,
    0.90,
    0.89,
    0.88,
    0.87,
    0.86,
    0.85,
    0.84,
    0.83,
    0.82,
    0.81,
    0.80,
    0.79,
    0.78,
    0.77,
    0.76,
    0.75,
    0.74,
    0.73,
]
accuracy = [
    0.97,
    0.96,
    0.95,
    0.94,
    0.93,
    0.92,
    0.91,
    0.90,
    0.89,
    0.88,
    0.87,
    0.86,
    0.85,
    0.84,
    0.83,
    0.82,
    0.81,
    0.80,
    0.79,
    0.78,
    0.77,
    0.76,
    0.75,
    0.74,
]

x = np.arange(len(time_elapsed))

fig, ax1 = plt.subplots(figsize=(14, 7))

color = "tab:purple"
ax1.set_xlabel("Index", fontsize=20)
ax1.set_ylabel("Elapsed Time (seconds)", color=color, fontsize=18)
ax1.bar(x, time_elapsed, color=color, alpha=0.6, label="Time Elapsed (s)")
ax1.tick_params(axis="y", labelcolor=color)
ax1.tick_params(axis="x", labelsize=16)
ax1.tick_params(axis="y", labelsize=16)

ax2 = ax1.twinx()
ax2.set_ylabel("Performance Metrics (%)", fontsize=20)
ax2.plot(x, precision, "r-o", label="Precision (%)", linewidth=2)
ax2.plot(x, recall, "g-o", label="Recall (%)", linewidth=2)
ax2.plot(x, f1_score, "m-o", label="F1-Score (%)", linewidth=2)
ax2.plot(x, accuracy, "b-o", label="Accuracy (%)", linewidth=2)
ax2.tick_params(axis="y", labelsize=16)
ax2.set_ylim(0, 1)

fig.tight_layout()
fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9), fontsize=16)
plt.title("Performance Metrics and Elapsed Time", fontsize=18)
plt.show()
