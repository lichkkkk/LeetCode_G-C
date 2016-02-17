__author__ = 'liuxiyun'

# Put each number in its right place.
# For example:
# When we find 5, then swap it with A[4].
# At last, the first place where its number is not right, return the place + 1.

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        for i in range(0,n):
            while nums[i]>0 and nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                temp = nums[i]
                nums[i],nums[temp-1] = nums[temp-1],nums[i]
        for i in range(0,n):
            if nums[i]!=i+1:
                return i+1
        return n+1


c=Solution()
print c.firstMissingPositive([2,1])