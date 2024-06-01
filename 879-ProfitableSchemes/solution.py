'''3-D DP'''

class Solution:
    MODULO_BASE = 1e9 + 7

    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        '''
          f(i, n, p) = # of schemas for profit[i:] with n members to achieve at least p profit
          f(i, n, p) = f(i+1, n, p) + f(i+1, n-group[i], p-profit[i])
          
          f(i, n, p) = 0 if n <= 0 
          f(len(p), n, p) = 1 if (n >= 0 and p <= 0) else 0
        '''
        cache = [[[-1] * (minProfit+1) for _ in range(n+1)] for _ in range(len(group))]
        return self.f(0, n, minProfit, group, profit, cache)

    def f(self, i, n, p, group, profit, cache):
        # print(i, n, p) 
        p = max(0, p)  # negative p is no different than p == 0, this makes caching easier
        if n < 0: return 0
        if n == 0 or i == len(group): return 1 if p == 0 else 0
        if cache[i][n][p] != -1: return cache[i][n][p]
        cache[i][n][p] = (self.f(i+1, n, p, group, profit, cache)
                          + self.f(i+1, n-group[i], p-profit[i], group, profit, cache))
        return int(cache[i][n][p] % self.MODULO_BASE)
