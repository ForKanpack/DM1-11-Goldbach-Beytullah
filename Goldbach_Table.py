import matplotlib.pyplot as plt
import pandas as pd


def primeCheck(x):  # Check if the number is prime
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


def all_pairs(x):  # Find the Goldbach pairs
    pairs = []
    for i in range(2, x // 2 + 1):
        if primeCheck(i) and primeCheck(x - i):
            pairs.append((i, x - i))
    return pairs


def main():
    x = int(input("Enter an even number greater than or equal to four: "))

    if x < 4 or x % 2 != 0:  # Validate the input
        print("Please enter an even number greater than or equal to four.")
        return

    pairs_count = []
    numbers = []

    for num in range(4, x + 1, 2):
        prime_pairs = all_pairs(num)
        pairs_count.append(len(prime_pairs))
        numbers.append(num)

    #DataFrame
    df = pd.DataFrame({
        'Numbers': numbers,
        'Number of Goldbach Pairs': pairs_count
    })

    # Split into two parts
    mid_index = len(df) // 2
    df1 = df.iloc[:mid_index]
    df2 = df.iloc[mid_index:]

    # First Table
    if not df1.empty:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=df1.values, colLabels=df1.columns, loc='center', cellLoc='center')
        plt.title('Goldbach Pairs (First Half)')
        plt.show()

    # Second Table
    if not df2.empty:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.axis('tight')
        ax.axis('off')
        ax.table(cellText=df2.values, colLabels=df2.columns, loc='center', cellLoc='center')
        plt.title('Goldbach Pairs (Second Half)')
        plt.show()


main()
