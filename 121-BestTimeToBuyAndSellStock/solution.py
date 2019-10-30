"""
    Key Points:
        The problem is asking us to find the largest diff between numbers in the list,
        and requirs the smaller num appears before the larger number. To solve this,
        we can scan the list from left to right, always memorizing the smallest number
        we have seen so far. When we see a number larger than current smallest number,
        we just calculate the diff and update the best profit we have seen.
        
    How to improve:
        The current implementation is already the most efficient one, which can finish in
        linear time. However, if the input prices are very large, given the prices
        should be continuous, we may be able to down sample the input first, and then
        narrow down the zone to search for the max profit.
"""
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
        for i in xrange(1, len(prices)):
            prevMinPrice = min(prevMinPrice, prices[i]) # update the lowest price we have seen so far
            currMaxProfit = max(currMaxProfit, prices[i] - prevMinPrice) # update the max possible profit so far
        return currMaxProfit
