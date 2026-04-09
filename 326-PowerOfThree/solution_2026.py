class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n >= 3:
            res = n % 3
            if not res:
                n = n // 3
            else:
                return False
        return n == 1
