class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for p in prices:
            if p < minPrice:
                minPrice = p
            if p - minPrice > maxProfit:
                maxProfit = p - minPrice
        return maxProfit