__author__ = 'liuxiyun'
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers)-1
        while i<j:
            tempsum = numbers[i]+numbers[j]
            if tempsum == target:
                return [i+1,j+1]
            elif tempsum<target:
                i+=1
            else:
                j-=1