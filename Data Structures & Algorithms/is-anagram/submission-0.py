class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0]*26
        for a in s: 
            arr[ord(a) - ord('a')] += 1
        for a in t: 
            arr[ord(a) - ord('a')] -= 1
        for a in arr: 
            if a != 0:
                return False
        return True
        