class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [], []
        prefix.append(nums[0])
        suffix.append(nums[-1])
        for i in range(1, len(nums) - 1):
            prefix.append(prefix[-1] * nums[i])
            suffix.append(suffix[-1] * nums[-(i + 1)])
        prefix.insert(0, 1)
        suffix.insert(0, 1)
        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[-(i + 1)])
        return res