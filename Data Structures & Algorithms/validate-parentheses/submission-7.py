class Solution:
    def isValid(self, s: str) -> bool:
        d = {"}" : "{", ")" : "(", "]" : "["}
        stack = []
        for ch in s:
            if ch == "{" or ch == "(" or ch == "[":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if top != d[ch]:
                    return False
        return True if len(stack) == 0 else False