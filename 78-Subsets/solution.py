class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      if len(nums) == 0:
        return [[]]
      res= []
      ss = self.subsets(nums[1:])
      for s in ss:
        res.append(s)
        res.append(s + [nums[0]])
      return res
