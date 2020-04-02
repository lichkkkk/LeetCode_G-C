"""
1306. Jump Game III
A DFS/Recursion solution.
licha@London, Apr. 2, 2020
"""
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
      if start < 0 or start >= len(arr) or arr[start] < 0:
        return False
      elif arr[start] == 0:
        return True
      else:
        next_pos_1, next_pos_2 = start - arr[start], start + arr[start]
        arr[start] = -1
        return self.canReach(arr, next_pos_1) or self.canReach(arr, next_pos_2)
