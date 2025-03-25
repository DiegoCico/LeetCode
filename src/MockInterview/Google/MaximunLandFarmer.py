from typing import List

def maximum_land(matrix: List[List[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    max_side = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1]
                    ) + 1
                max_side = max(max_side, dp[i][j])

    print(dp)
    return max_side * max_side

def maximum_land_prints(matrix: List[List[int]]) -> int:
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(cols)] for _ in range(rows)]
    max_side = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    # Get minimum of top, left, and top-left neighbors
                    top = dp[i - 1][j]
                    left = dp[i][j - 1]
                    top_left = dp[i - 1][j - 1]
                    dp[i][j] = min(top, left, top_left) + 1

                    print(f"Updating dp[{i}][{j}]: min(top={top}, left={left}, top-left={top_left}) + 1 = {dp[i][j]}")

                # Update max_side if needed
                if dp[i][j] > max_side:
                    print(f"New max square side found at ({i},{j}) with side length = {dp[i][j]}")
                    max_side = dp[i][j]
            else:
                print(f"matrix[{i}][{j}] is 0 → no square ends here.")

    print("\nFinal DP matrix:")
    for row in dp:
        print(row)

    print(f"\nLargest square side length = {max_side}")
    print(f"Largest square area = {max_side * max_side}")
    return max_side * max_side


matrix = [
    [0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

print(maximum_land_prints(matrix))  # Output: 9

# The goal is to find the largest square (not island) formed entirely by 1s in a binary matrix.

# We use dynamic programming to keep track of the largest square that ends at each (i, j).
# dp[i][j] will store the side length of the biggest square ending at that cell.

# If the cell at (i, j) is a 1, we check its top (i-1, j), left (i, j-1), and top-left (i-1, j-1) neighbors.
# The smallest of those three values plus 1 becomes dp[i][j].

# For example, if all three neighbors have squares of side length 2, then (i, j) can form a 3x3 square.

# We track the largest side length seen during this process in the max_side variable.
# Finally, we return the area, which is max_side ** 2.

# Time complexity is O(m * n) because we iterate through every cell once.
# Space complexity is also O(m * n) for the DP matrix, but it can be optimized to O(n) if needed.
