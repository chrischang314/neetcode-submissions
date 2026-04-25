class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex = 0
        for i, n in enumerate(nums):
            if i <= maxIndex:
                maxIndex = max(maxIndex, i + n)
        return maxIndex >= len(nums) - 1
