class Solution:
    def rob(self, nums: List[int]) -> int:
      if len(nums) == 0:
        return 0
      if len(nums) == 1:
        return nums[0]
      return max(nums[0]+self.rob_no_cycle(nums[2:-1]), self.rob_no_cycle(nums[1:]))
      
    def rob_no_cycle(self, nums: List[int]) -> int:
      if len(nums) == 0:
        return 0
      if len(nums) == 1:
        return nums[0]
      table = [0] * len(nums)
      table[0] = nums[0]
      table[1] = max(nums[0], nums[1])
      for i in range(2, len(nums)):
        table[i] = max(table[i-1], table[i-2] + nums[i])
      return table[-1]
