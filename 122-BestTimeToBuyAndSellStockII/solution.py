"""
    Key Points:
        The best strategy here is to capture all price increases. That means,
        as long as today's price is higher than yesterday's, we do a transaction.
        If today's price is lower or equal to yesterday's, we just move to the
        next day. Another way to understand this is, we transform the input of
        prices to the price diff of every day, e.g. [1,3,2,4] -> [0,+2,-1,+2].
        Then we sum up all positive numbers in the list.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        profit = 0
        prev_price = prices[0]
        for price in prices: # iterate all prices sequentially
            if price > prev_price: # if there is an increase
                profit += (price - prev_price) # add the increase to the profit
            prev_price = price # use the new proice as the reference point
        return profit
