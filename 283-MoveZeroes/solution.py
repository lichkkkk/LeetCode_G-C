class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        curr_idx = 0
        for i in range(len(nums)):
          if nums[i] != 0:
            nums[curr_idx] = nums[i]
            curr_idx += 1
        for i in range(curr_idx, len(nums)):
          nums[i] = 0
