class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum, cursum = float("-inf"), 0
        for n in nums:
            cursum += n
            maxsum = max(maxsum, cursum)
            cursum = max(0, cursum)
        return maxsum