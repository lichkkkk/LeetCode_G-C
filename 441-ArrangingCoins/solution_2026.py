class Solution:
    def coinsSum(self, level: int) -> int:
        return (1 + level) * level // 2

    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        if n == 1: return 1
        while l + 1 < r:
            mid = (l + r) // 2
            coin_cnt = self.coinsSum(mid)
            if coin_cnt < n:
                l = mid
            elif coin_cnt > n:
                r = mid
            else:
                return mid
        return l
