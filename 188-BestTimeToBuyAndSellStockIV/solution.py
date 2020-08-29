class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        # special case, otherwise TLE
        if k > len(prices) // 2:
            return sum([max(0, prices[i] - prices[i-1]) for i in range(1, len(prices))])
        # table[i][j] => best profit by day j with at most i transactions
        table = [[0] * len(prices) for i in range(k+1)]
        for i in range(1, k+1):
            best_hold_pos = -prices[0]
            for j in range(1, len(prices)):
                best_hold_pos = max(best_hold_pos, table[i-1][j] - prices[j])
                table[i][j] = max(table[i][j-1], best_hold_pos + prices[j])
        return table[-1][-1]
