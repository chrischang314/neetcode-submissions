class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start, end = {}, {}
        for i, c in enumerate(s):
            if c not in start:
                start[c] = i
                end[c] = i
            end[c] = max(end[c], i)
        
        res = []
        l, r = 0, 0
        while r < len(s):
            curStart, curEnd = l, r
            while curStart <= curEnd:
                c = s[curStart]
                curEnd = max(curEnd, end[c])
                curStart += 1
            res.append(curEnd - l + 1)
            l, r, = curStart, curStart
        return res

