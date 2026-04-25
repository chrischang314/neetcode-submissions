class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        def dfs(i, j):
            if i >= rows or i < 0 or j >= cols or j < 0 or not grid[i][j]: 
                return 1
            if (i, j) in visited:
                return 0
            visited.add((i, j))
            return + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return dfs(i, j)
        
        