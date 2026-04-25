class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        delta = [g - c for g, c in zip(gas, cost)]
        cursum = 0
        res = 0
        for i, d in enumerate(delta):
            cursum += d
            if cursum < 0:
                cursum = 0
                res = i + 1
        return res