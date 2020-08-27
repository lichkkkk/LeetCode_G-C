"""
licha in London, Aug. 28, 2020
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        # find the first "falling edge" from the end
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        if i == -1:
            nums.sort()
            return
        targetIndex = i
        # find the least one larger than the num to replace
        i += 1
        while i+1 < len(nums) and nums[i+1] > nums[targetIndex]:
            i += 1
        # swap
        tmp = nums[targetIndex]
        nums[targetIndex] = nums[i]
        nums[i] = tmp
        # reverse nums[targetIndex+1:]
        nums[targetIndex+1:] = reversed(nums[targetIndex+1:])
