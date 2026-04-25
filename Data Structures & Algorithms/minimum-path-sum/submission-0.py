class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = {(rows - 1, cols - 1): grid[rows - 1][cols - 1]}
        
        def dfs(i, j):
            if i >= rows or j >= cols:
                return float("inf")
            if (i, j) in dp:
                return dp[(i, j)]
            dp[(i, j)] = min(dfs(i + 1, j), dfs(i, j + 1)) + grid[i][j]
            return dp[(i, j)]
        res = dfs(0, 0)
        return res