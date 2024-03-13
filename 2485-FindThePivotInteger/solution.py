# BinarySearch

class Solution:

  def _get_sum(self, start: int, end: int) -> int:
    assert 0 < start <= end
    return (start + end) * (end - start + 1) / 2

  def pivotInteger(self, n: int) -> int:
    if n == 1:
      return 1
    # otherwise, the answer cannot be either left or righ
    left = 1
    right = n
    while right > left + 1:
      mid = (left + right) // 2
      left_sum = self._get_sum(1, mid)
      right_sum = self._get_sum(mid, n)
      if left_sum > right_sum:
        right = mid
      elif left_sum < right_sum:
        left = mid
      else:
        return mid
    return -1
