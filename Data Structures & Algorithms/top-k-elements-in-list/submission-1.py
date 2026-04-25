class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        tmp = [[] for i in range(len(nums) + 1)] # need the +1 because n + 1 possible counts from 0 to n
        for key, value in counts.items():
            tmp[value].append(key)
        res = []
        for i in range(len(tmp) - 1, -1, -1):
            res.extend(tmp[i])
            if len(res) == k:
                return res