class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # NOTE: truncate toward zero also needs to be from negative side
        stack = []
        for t in tokens: 
            if t in ["+", "-", "*", "/"]:
                y, x = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(x + y)
                elif t == "-":
                    stack.append(x - y)
                elif t == "*":
                    stack.append(x * y)
                else: 
                    stack.append(int(x / y))
            else: 
                stack.append(int(t))
        return stack[-1]