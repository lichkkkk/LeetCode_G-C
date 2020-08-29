"""
A DP solution like 188 can be faster, but this one is simpler
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        table1 = [0] * len(prices)
        curr_min = prices[0]
        for i in range(1, len(prices)):
            table1[i] = max(table1[i-1], prices[i] - curr_min)
            curr_min = min(curr_min, prices[i])
        table2 = [0] * len(prices)
        curr_max = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            table2[i] = max(table2[i+1], curr_max - prices[i])
            curr_max = max(curr_max, prices[i])
        return max([table1[i] + table2[i] for i in range(len(prices))])
