"""
Key Points:
    1. The approach to determine whether we are looping endlessly, is to
    check whether the number appeared before in this loop.
    2. We can use a Set to memorize all number appeared in this loop.
    3. Given a number, to compute the next replacement of it, we can use
    a loop, every time we get the mod and divide the number by 10, until
    it's 0.
"""
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
                n = n // 10
            n = nextNum
        return n == 1
