# recursion
class Solution:
    def convertToBase7(self, num: int) -> str:
        prefix = '-' if num < 0 else ''
        num = abs(num)
        if num < 7:
          return prefix + str(num)
        else:
          return prefix + self.convertToBase7(num // 7) + str(num % 7)
