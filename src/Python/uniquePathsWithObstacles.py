class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * cols for _ in range(rows)]

        seen = False
        for j in range(cols):
            if obstacleGrid[0][j] == 1:
                seen = True
            dp[0][j] = 0 if seen else 1

        seen = False
        for i in range(rows):
            if obstacleGrid[i][0] == 1:
                seen = True
            dp[i][0] = 0 if seen else 1

        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        print(dp)
        return dp[rows - 1][cols - 1]
