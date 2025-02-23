class Solution:

    def helper(self, nums, start, end, cache) -> int:
      key = (start, end)
      if key in cache:
          return cache[key]
      if start == end:
          return nums[start]
      res1 = nums[start] - self.helper(nums, start + 1, end, cache)
      res2 = nums[end] - self.helper(nums, start, end - 1, cache)
      res = max(res1, res2)
      cache[key] = res
      return res


    def predictTheWinner(self, nums: List[int]) -> bool:
      cache = {}
      res = self.helper(nums, 0, len(nums) - 1, cache) >= 0
      # print(cache)
      return res
