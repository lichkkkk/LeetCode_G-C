__author__ = 'liuxiyun'

# My idea is to use two pointers i,j
# let i points to the first zero and j points to the first non-zero number on the right to i. swap them.
# Time: O(n)

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i,j=0
        while j<n:
            while i<n and nums[i]!=0:
                i+=1
            j=i
            while j<n and nums[j]==0:
                j+=1
            nums[i],nums[j]=nums[j],nums[i]

# Move all non-zeroes forward, and fill the rest of the list with 0
# Much faster than the first one
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        for num in nums:
            if num!=0:
                nums[i]=num
                i+=1
        for j in range(i,len(nums)):
            nums[j]=0
# Test case:
# # [0]
# # [0,1,2]
# # [1,0,2]
# # [0,0,0]
# # [1,2,3]