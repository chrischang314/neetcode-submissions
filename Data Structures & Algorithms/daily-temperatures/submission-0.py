class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if not stack: 
                stack.append([t, i])
            elif t <= stack[-1][0]:
                stack.append([t, i])
            else: 
                while stack and t > stack[-1][0]:
                    tmpt, tmpi = stack.pop()
                    res[tmpi] = i - tmpi
                stack.append([t, i])
        return res
