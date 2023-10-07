def uniquePathsWithObstacles(obstacleGrid):
    if not obstacleGrid or not obstacleGrid[0]:
        return 0

    m, n = len(obstacleGrid), len(obstacleGrid[0])
    
    # Initialize a 2D DP array to store the number of unique paths
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the top-left cell
    dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
    
    # Fill in the first row
    for j in range(1, n):
        if obstacleGrid[0][j] == 0:
            dp[0][j] = dp[0][j - 1]
    
    # Fill in the first column
    for i in range(1, m):
        if obstacleGrid[i][0] == 0:
            dp[i][0] = dp[i - 1][0]
    
    # Fill in the rest of the DP array
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    return dp[m - 1][n - 1]

# Test cases
obstacleGrid1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
obstacleGrid2 = [[0, 1], [0, 0]]
print(uniquePathsWithObstacles(obstacleGrid1))  # Output: 2
print(uniquePathsWithObstacles(obstacleGrid2))  # Output: 1
