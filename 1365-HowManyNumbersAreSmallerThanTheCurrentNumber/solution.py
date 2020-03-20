class Solution:
  def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    sorted_copy = sorted(nums.copy())
    smaller_count_map = {}
    for i in range(len(sorted_copy)):
      curr_num = sorted_copy[i]
      if curr_num not in smaller_count_map:
        smaller_count_map[curr_num] = i
    res = [smaller_count_map[num] for num in nums]
    return res
