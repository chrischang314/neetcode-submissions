class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = {(rows - 1, cols - 1):1}

        def dfs(i, j):
            if i >= rows or j >= cols or obstacleGrid[i][j] != 0:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            else: 
                dp[(i, j)] = dfs(i, j + 1) + dfs(i + 1, j)
                return dp[(i, j)]
        
        return dfs(0, 0)
            

        