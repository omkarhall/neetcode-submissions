class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '{' or ch == '(' or ch == '[':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if ch == '}':
                    if top != '{':
                        return False
                elif ch == ')':
                    if top != '(':
                        return False
                elif ch == ']':
                    if top != '[':
                        return False
        if len(stack) == 0:
            return True
        return False