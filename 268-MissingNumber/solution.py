"""
This also works for input with duplicates/gap between numbers
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            curr_num = nums[i]
            curr_idx = i
            while curr_num != curr_idx and curr_num < len(nums):
                next_num = nums[curr_num]
                nums[curr_num] = curr_num
                curr_idx = curr_num
                curr_num = next_num
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
