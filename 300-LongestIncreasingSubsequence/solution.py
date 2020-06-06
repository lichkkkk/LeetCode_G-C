"""
This is a less-perfect O(n^2) solution. Just as a reference.
This problem can be solved within O(nlogn).
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
      if len(nums) == 0:
        return 0
      # table[i] = LIS's length whose last num is nums[i]
      table = [0] * len(nums)
      for i in range(len(table)):
        table [i] = 1
        for j in range(0, i):
          if nums[j] < nums[i]:
            table[i] = max(table[i], table[j] + 1)
      return max(table)
