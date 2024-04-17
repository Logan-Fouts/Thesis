import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

sizes = np.array([300, 900, 1500, 3000])
times = np.array([4.4, 12.1, 28.9, 109])


def poly_func(x, a, b, c):
    return a * x**2 + b * x + c


popt, pcov = curve_fit(poly_func, sizes, times)

PREDICT_SIZE = 17500
predicted_time = poly_func(PREDICT_SIZE, *popt)
print(f"Predicted time for size {PREDICT_SIZE}: {predicted_time:.2f} seconds")

# Plotting
plt.figure(figsize=(10, 5))
plt.scatter(sizes, times, color="red", label="Original Data")
sizes_line = np.linspace(min(sizes), max(sizes) * 6, 400)
times_fit = poly_func(sizes_line, *popt)
plt.plot(sizes_line, times_fit, label="Fitted Curve", color="blue")
plt.scatter(
    PREDICT_SIZE,
    predicted_time,
    color="green",
    label=f"Predicted time for size {PREDICT_SIZE}",
)

plt.title("Fingerprint Results")
plt.xlabel("Size")
plt.ylabel("Time (s)")
plt.legend()
plt.grid(True)
plt.show()
