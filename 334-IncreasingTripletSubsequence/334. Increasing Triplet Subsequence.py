__author__ = 'liuxiyun'
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<=2:
            return False
        i= 0
        while i<len(nums)-1 and nums[i]>=nums[i+1]:
            i+=1
        if i == len(nums)-1:
            return False
        a = nums[i]
        b = nums[i+1]
        least = a
        i+=2
        while i<len(nums):
            if nums[i]>b:
                return True
            elif a<nums[i]<=b:
                b=nums[i]
            elif least<nums[i]<=a:
                a = least
                b = nums[i]
            else: # nums[i]<=least
                least = nums[i]
            i+=1
        return False