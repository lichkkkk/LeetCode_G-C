class Solution:
    def search(self, nums: List[int], target: int) -> int:
      if len(nums) < 1 or nums[0] > target or nums[-1] < target:
        return -1;
      if nums[0] == target:
        return 0
      if nums[-1] == target:
        return len(nums) - 1
      l, r = 0, len(nums) - 1
      while l + 1 < r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
          return mid
        elif nums[mid] > target:
          r = mid
        else:
          l = mid
      return -1
