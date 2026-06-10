class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        nextBuy = nextSell = 0
        curBuy = curSell = 0
        for i in range(n - 1, -1, -1):
            curBuy = max(nextSell - prices[i], nextBuy)
            curSell = max(nextBuy + prices[i], nextSell)
            nextBuy = curBuy
            nextSell = curSell
        return curBuy
