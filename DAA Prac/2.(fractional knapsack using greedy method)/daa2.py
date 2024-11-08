def fractional_knapsack(value, weight, capacity):
    items = sorted(zip(value, weight), key=lambda x: x[0] / x[1], reverse=True)
    total_value = 0

    for v, w in items:
        if capacity >= w:
            total_value += v
            capacity -= w
        else:
            total_value += v * (capacity / w)
            break

    return total_value


def get_input():
    value = list(map(int, input("Enter the values (comma-separated): ").split(',')))
    weight = list(map(int, input("Enter the weights (comma-separated): ").split(',')))
    capacity = int(input("Enter the capacity of the knapsack: "))

    return value, weight, capacity


if __name__ == "__main__":
    value, weight, capacity = get_input()
    result = fractional_knapsack(value, weight, capacity)
    print(f"Maximum value in knapsack: {result}")
