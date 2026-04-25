class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        scount = Counter(s)
        tcount = Counter(t)
        for key in scount: 
            if scount[key] != tcount[key]:
                return False
        return True
        