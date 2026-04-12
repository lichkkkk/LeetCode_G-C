class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x
        # l < root < r
        l, r = 0, x
        # such that mid != l or r
        while l + 1 < r:
            mid = (l + r) // 2
            square = mid ** 2
            if square == x:
                return mid
            elif square > x:
                r = mid
            else:
                l = mid
        return l
