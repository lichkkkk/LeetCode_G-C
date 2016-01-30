__author__ = 'liuxiyun'
# Thanks to Chang's instruction, my mom won't be worried about my Binary Search anymore!
# O(log n)
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # edge case: x=0,1
        if x == 0:
            return 0
        if x == 1:
            return 1
        start = 1 # always points to the number smaller than the square root of x
        end = x/2+1# always points to the number larger than the square root of x
        while start +1 < end:
            mid = start + (end-start)/2
            temp = mid*mid
            if temp == x:
                return mid
            elif temp < x:
                start = mid
            else:
                end = mid
        return start
# Test case:
# # 0,1,2,3,4,5