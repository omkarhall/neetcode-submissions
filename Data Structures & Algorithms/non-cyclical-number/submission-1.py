class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            res = 0
            for digit in str(n):
                res += int(digit) ** 2
            return res
        d = {}
        while n != 1:
            n = sumOfSquares(n)
            if n in d:
                return False
            d[n] = 1
        return True