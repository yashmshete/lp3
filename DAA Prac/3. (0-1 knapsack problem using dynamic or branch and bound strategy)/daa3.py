def knapsack_dp(value, weight, capacity):
    n = len(value)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weight[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight[i - 1]] + value[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


def get_input():
    value = list(map(int, input("Enter the values (comma-separated): ").split(',')))
    weight = list(map(int, input("Enter the weights (comma-separated): ").split(',')))
    capacity = int(input("Enter the capacity of the knapsack: "))

    return value, weight, capacity


if __name__ == "__main__":
    value, weight, capacity = get_input()
    result = knapsack_dp(value, weight, capacity)
    print(f"Maximum value in knapsack: {result}")
