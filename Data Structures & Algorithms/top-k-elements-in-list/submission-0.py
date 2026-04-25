class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        tmp = [[] for i in range(len(nums) + 1)]
        for key, value in counts.items():
            tmp[value].append(key)
        res = []
        for i in range(len(tmp) - 1, -1, -1):
            res.extend(tmp[i])
            if len(res) == k:
                return res