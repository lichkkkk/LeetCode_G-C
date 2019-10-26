class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        prevMinPrice = prices[0]
        currMaxProfit = 0
        for i in range(1, len(prices)):
            prevMinPrice = min(prevMinPrice, prices[i])
            currMaxProfit = max(currMaxProfit, prices[i] - prevMinPrice)
        return currMaxProfit
