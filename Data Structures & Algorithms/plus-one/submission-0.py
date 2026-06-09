class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        mul = 1
        for i in range(len(digits)-1,-1,-1):
            res += digits[i] * mul
            mul *= 10
        res += 1
        newD = []
        for ch in str(res):
            newD.append(ch)
        return newD