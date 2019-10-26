class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        appearedNumSet = set()
        while n != 1 and n not in appearedNumSet:
            appearedNumSet.add(n)
            nextNum = 0
            while n > 0:
                nextNum += (n % 10) ** 2
                n = int(n / 10)
            n = nextNum
        return n == 1
