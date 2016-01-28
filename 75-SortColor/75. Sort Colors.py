__author__ = 'liuxiyun'

# Three pointers
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p1 = 0 # points to 0
        p2 = len(nums)-1 # points to 2
        i = 0
        # decide where should i go
        while i <= p2:# p2 points to the next position that need to set '2', that's why need"="
            while i<p2 and nums[i] == 2:
                nums[i],nums[p2] = nums[p2],nums[i]
                p2-=1 # p2 points to the next position that need to set '2'
            while i>p1 and nums[i] == 0:
                nums[i],nums[p1] = nums[p1],nums[i]
                p1+=1
            i+=1