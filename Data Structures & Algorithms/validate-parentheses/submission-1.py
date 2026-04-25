class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {")":"(", "]":"[", "}":"{"}
        for c in s: 
            if c in ["(", "[", "{"]:
                stack.append(c)
            else: 
                if stack and stack[-1] == par[c]:
                    stack.pop(-1)
                else: 
                    return False
        return not stack
            