import matplotlib.pyplot as plt

# Data
numbers = [
    4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40,
    42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78,
    80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100
]
goldbach_pairs = [
    1, 1, 1, 2, 1, 2, 2, 2, 2, 3, 3, 3, 2, 3, 2, 4, 4, 2, 3, 4, 3, 4, 5, 4, 3,
    5, 3, 4, 6, 3, 5, 6, 2, 5, 6, 5, 5, 7, 4, 5, 8, 5, 4, 9, 4, 5, 7, 3, 6
]

# Charting
plt.figure(figsize=(12, 6))
plt.plot(numbers,
         goldbach_pairs,
         marker="o",
         linestyle="-",
         color="black",
         label="Goldbach Pairs")

# Arrangements
plt.title("The Distribution of Goldbach Pairs by Numbers", fontsize=14)
plt.xlabel("Numbers", fontsize=12)
plt.ylabel("Number of Goldbach Pairs", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()
plt.tight_layout()

# Show the chart
plt.show()