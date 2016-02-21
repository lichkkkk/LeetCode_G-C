__author__ = 'liuxiyun'
# Insert lower-1 and upper+1 into the list
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        nums.insert(0,lower-1)
        nums.append(upper+1)
        res = []
        i = 0
        while i<len(nums)-1:
            left,right = nums[i],nums[i+1]
            if left!=right-1:
                if right-left==2:
                    res.append(str(right-1))
                else:
                    res.append(str(left+1)+"->"+str(right-1))
            i=i+1
        return res

c=Solution()
c.findMissingRanges([2],0,9)
c.findMissingRanges([],1,1)
c.findMissingRanges([0,1,3,50,75],0,99)
c.findMissingRanges([-1],-1,0)