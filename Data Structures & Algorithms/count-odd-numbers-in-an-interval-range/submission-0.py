class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = (high - low) // 2
        count += (low % 2 == 1 or high % 2 == 1)
        return count