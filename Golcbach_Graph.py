import matplotlib.pyplot as plt


def primeCheck(x):    #Check the number prime is
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


def all_pairs(x):    #Find the all pairs
    pairs = []
    for i in range(2, x // 2 + 1):
        if primeCheck(i) and primeCheck(x - i):
            pairs.append((i, x - i))
    return pairs


def main():
    x = int(input("Enter a number: "))
    x_values = []
    y_values = []


    for num in range(4, x + 1, 2):
        prime_pairs = all_pairs(num)
        differences = [pair[1] - pair[0] for pair in prime_pairs]

        for diff in differences:
            x_values.append(num)
            y_values.append(diff)

    # Graph
    plt.figure(figsize=(10, 6))  # Adjust the graph size
    plt.scatter(x_values, y_values, color='blue', s=9)
    plt.title('Differences of Goldbach Pairs for Even Numbers ') #Adjust the points
    plt.xlabel('Numbers')
    plt.grid(True)
    plt.show()


main()
