__author__ = 'liuxiyun'
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# check low and high
# alwasy set low to the correct version and high to the bad version\
# Time: log n
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        if isBadVersion(low) == True:
            return low
        while low+1 < high:
            mid = low + (high-low)/2
            if isBadVersion(mid) == True:
                high = mid
            else:
                low = mid
        return high
# Test case:
# [0,0,0,0,0,1]
# [1,1,1,1,1,1]
# [1]
# [0,0,1,1,1,1]