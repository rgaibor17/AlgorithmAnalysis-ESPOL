def knapsack_01_with_matrix(weights, values, capacity):
    """Original version with 2D DP table and matrix display"""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the dp table
    for i in range(1, n + 1):
        for j in range(capacity + 1):
            if weights[i - 1] <= j:  # Check if item can fit
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    # Display the DP matrix
    print("\n### DP Matrix ###")
    for row in dp:
        print(row)

    # Backtrack to find selected items
    selected_items = []
    j = capacity
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:  # If value comes from including item
            selected_items.append(i)
            j -= weights[i - 1]

    return dp[n][capacity], selected_items


def knapsack_01_fully_optimized(weights, values, capacity):
    """Fully optimized version with 1D DP array"""
    n = len(weights)
    dp = [0] * (capacity + 1)

    # Build the dp array
    for i in range(n):
        for j in range(capacity, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    # Backtrack to find selected items
    selected_items = []
    remaining_capacity = capacity
    for i in range(n - 1, -1, -1):
        if remaining_capacity >= weights[i] and dp[remaining_capacity] == dp[remaining_capacity - weights[i]] + values[i]:
            selected_items.append(i + 1)
            remaining_capacity -= weights[i]

    return dp[capacity], selected_items


# Desktop Tests
if __name__ == "__main__":
    print(f"\nTest Case 1")

    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5

    print(f"\nWeights: {weights}\nValues: {values}\nCapacity: {capacity}\n")

    print("### Original Algorithm ###")
    max_value, selected_items = knapsack_01_with_matrix(weights, values, capacity)
    print(f"Maximum Value: {max_value}")
    print(f"Selected Items: {selected_items}")

    print("\n### Fully Optimized Algorithm ###")
    max_value, selected_items = knapsack_01_fully_optimized(weights, values, capacity)
    print(f"Maximum Value: {max_value}")
    print(f"Selected Items: {selected_items}")

    print(f"\nAdditional Test Case 2")

    weights = [1, 2, 3, 8]
    values = [20, 30, 40, 100]
    capacity = 10

    print(f"\nWeights: {weights}\nValues: {values}\nCapacity: {capacity}\n")

    print("\n### Original Algorithm (Test 2) ###")
    max_value, selected_items = knapsack_01_with_matrix(weights, values, capacity)
    print(f"Maximum Value: {max_value}")
    print(f"Selected Items: {selected_items}")

    print("\n### Fully Optimized Algorithm (Test 2) ###")
    max_value, selected_items = knapsack_01_fully_optimized(weights, values, capacity)
    print(f"Maximum Value: {max_value}")
    print(f"Selected Items: {selected_items}")
