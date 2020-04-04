"""
39. Combination Sum
licha@London, Apr. 4th, 2020
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      candidates.sort()
      all_res = []
      self.helper([], 0, 0, target, candidates, all_res)
      return all_res
    
    def helper(self, curr_res, curr_sum, curr_pos, target, candidates, all_res):
      if curr_sum > target:
        return
      if curr_sum == target:
        all_res.append(curr_res.copy())
        return
      for i in range(curr_pos, len(candidates)):
        new_sum = curr_sum + candidates[i]
        if new_sum > target:
          # Because candidates is sorted, we can break early here
          # This reduced the runtime from 88ms to 44ms in Leetcode OJ
          break
        curr_res.append(candidates[i])
        self.helper(curr_res, new_sum, i, target, candidates, all_res)
        curr_res.pop()
