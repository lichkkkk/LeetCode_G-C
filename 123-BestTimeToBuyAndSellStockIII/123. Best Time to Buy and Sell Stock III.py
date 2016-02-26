__author__ = 'liuxiyun'
# left - list: the maximum profit from day 0 to day i
# right - list: the maximum profit from day i to day -1
# Add together to get the maximum profit with two transaction
# O(n)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_p = []
        left = self.maxProfit_help(prices)
        right = self.maxProfit_help2(prices)
        for i in range(len(prices)):
            max_p.append(left[i]+right[i])
        return max(max_p) if max_p!=[] else 0
    def maxProfit_help(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        min_price = prices[0]
        max_profit=0
        profit = [0]*len(prices)
        for i in range(len(prices)):
            if prices[i] <= min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i]-min_price)
            profit[i] = max_profit
        return profit
    def maxProfit_help2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        max_price = prices[-1]
        max_profit=0
        profit = [0]*len(prices)
        for i in range(len(prices)-1,-1,-1):
            if prices[i] >= max_price:
                max_price = prices[i]
            else:
                max_profit = max(max_profit, max_price-prices[i])
            profit[i] = max_profit
        return profit