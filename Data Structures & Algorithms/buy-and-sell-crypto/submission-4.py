class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j = 0
        minPrice = 101
        maxProfit = 0
        while j < len(prices):
            if prices[j] < minPrice:
                minPrice = prices[j]
            else:
                profit = prices[j] - minPrice
                maxProfit = max(profit, maxProfit)
            j += 1
        return maxProfit
            
