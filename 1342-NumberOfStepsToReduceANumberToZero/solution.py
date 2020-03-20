class Solution(object):
  def numberOfSteps (self, num):
    """
    :type num: int
    :rtype: int
    """
    if num == 1:
      return 1
    else:
      return self.numberOfSteps(num // 2) + num % 2 + 1

# test
solution = Solution()
print(solution.numberOfSteps(14))
