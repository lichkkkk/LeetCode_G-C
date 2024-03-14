# O(N) array

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
      # build a sum -> pos map
      pos_by_sum = [-1]  # trick to make the for loop cleaner
      curr_sum = 0
      for i in range(len(nums)):
        if nums[i] == 0:
          continue
        elif nums[i] == 1:
          curr_sum += 1
          pos_by_sum.append(i)
        else:
          raise ValueError('invalid nums')
      total_sum = len(pos_by_sum) - 1
      if total_sum < goal:
        return 0

      pos_by_sum.append(len(nums))  # trick to make the for loop cleaner
      res = 0
      if goal == 0:
        for i in range(1, len(pos_by_sum)):
          zero_cnt = pos_by_sum[i] - pos_by_sum[i-1] -1
          res += (1 + zero_cnt) * zero_cnt // 2
      else:
        for i in range(1, len(pos_by_sum) - goal):
          left_zero_cnt = pos_by_sum[i] - pos_by_sum[i-1] - 1
          right_zero_cnt = pos_by_sum[i+goal] - pos_by_sum[i+goal-1] - 1
          res += (left_zero_cnt + 1) * (right_zero_cnt + 1)
      return res
