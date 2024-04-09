import numpy as np

class Solution:
  def checkPerfectNumber(self, num: int) -> bool:
    if num == 1:
      return False
    root = int(np.sqrt(num))
    divisors = [1]
    for i in range(2, root + 1):
      if num % i:
        continue
      divisors.append(i)
      divisors.append(num // i)
    return sum(divisors) == num
