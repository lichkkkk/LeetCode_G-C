class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        res = False
        while n > 1:
            mid = 2**(n-1)
            if k > mid:
                k = 2**n - k
                res = not res
            elif k == mid:
                res = not res
                break
            n -= 1
        return "1" if res else "0"
