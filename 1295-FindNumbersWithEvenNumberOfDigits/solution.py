class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([self.countDigits(num) % 2 == 0 for num in nums])
    
    @staticmethod
    def countDigits(num):
        if num < 1:
            return 0
        res = 0
        while num > 0:
            num //= 10
            res += 1
        return res
