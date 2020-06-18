"""
code can be easier if we use two pointers
"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        goodStart = 0;
        alreadyBad = False
        for i in range(len(nums)):
          if len(stack) > 0 and stack[-1] > nums[i]:
            while len(stack) > 0 and stack[-1] > nums[i]:
              stack.pop()
            goodStart = len(stack)
            alreadyBad = True
          elif not alreadyBad:
            stack.append(nums[i])
        if len(stack) == len(nums):
          return 0
        stack = []
        goodEnd = 0;
        alreadyBad = False
        for i in range(len(nums)-1, -1, -1):
          if len(stack) > 0 and stack[-1] < nums[i]:
            while len(stack) > 0 and stack[-1] < nums[i]:
              stack.pop()
            goodEnd = len(stack)
            alreadyBad = True
          elif not alreadyBad:
            stack.append(nums[i])
        return len(nums) - goodStart - goodEnd
