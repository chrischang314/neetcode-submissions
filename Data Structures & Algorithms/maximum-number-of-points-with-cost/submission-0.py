class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        dp = [[0] * cols for i in range(rows)]
        for i in range(cols):
            dp[0][i] = points[0][i]
        for i in range(1, rows):
            for j in range(cols):
                curmax = float("-inf")
                for k in range(cols):
                    curmax = max(curmax, points[i][j] + dp[i - 1][k] - abs(k - j))
                dp[i][j] = curmax
        return max(dp[-1])