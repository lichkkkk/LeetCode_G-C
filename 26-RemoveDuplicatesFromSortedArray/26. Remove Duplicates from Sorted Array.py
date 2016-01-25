__author__ = 'liuxiyun'

# Move forward
# Time: O(n)
# Space: O(1)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        re = 0
        for i in range(len(nums)):
            if i == len(nums)-1:
                nums[re] = nums[i]
                re +=1
                break
            if nums[i] == nums[i+1] :
                continue
            else:
                nums[re] = nums[i]
                re +=1
        return re

# Test case:
# # []
# # [1,1,2]
# # [1,2,3]
# # [1,2,2]