class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        lowest_p = prices[0]
        for p in prices:
            best = max(best, p - lowest_p)
            lowest_p = min(p, lowest_p)
        return best
