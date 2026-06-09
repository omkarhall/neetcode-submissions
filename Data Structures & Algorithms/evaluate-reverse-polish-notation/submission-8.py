class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for t in tokens:
            if t == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                res = n2 + n1
                stack.append(res)
            elif t == "-":
                n1 = stack.pop()
                n2 = stack.pop()
                res = n2 - n1
                stack.append(res)
            elif t == "*":
                n1 = stack.pop()
                n2 = stack.pop()
                res = n2 * n1
                stack.append(res)
            elif t == "/":
                n1 = stack.pop()
                n2 = stack.pop()
                res = int(n2 / n1)
                stack.append(res)
            else:
                stack.append(int(t))
        return stack.pop()
        