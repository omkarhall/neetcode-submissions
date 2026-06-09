class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for t in tokens:
            if t == "+":
                x = stack.pop()
                y = stack.pop()
                res = y + x
                stack.append(res)
            elif t == "-":
                x = stack.pop()
                y = stack.pop()
                res = y - x
                stack.append(res)
            elif t == "*":
                x = stack.pop()
                y = stack.pop()
                res = y * x
                stack.append(res)
            elif t == "/":
                x = stack.pop()
                y = stack.pop()
                res = int(y / x)
                stack.append(res)
            else:
                stack.append(int(t))
                
        return stack.pop()