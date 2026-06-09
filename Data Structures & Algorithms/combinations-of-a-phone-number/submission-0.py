class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        def backtrack(i, combo):
            if i == len(digits):
                res.append(combo)
                return
            for ch in letters[digits[i]]:
                backtrack(i+1, combo + ch)
        if digits:
            backtrack(0,"")
        return res


