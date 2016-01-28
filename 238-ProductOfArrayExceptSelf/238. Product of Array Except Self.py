__author__ = 'liuxiyun'

# O(1)
# Create two list. One is the product of all the number before this number
# One is the product of all the number after this number
#At last, multiply each number from those two list which is in the same position

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product_left = [1 for i in range(len(nums))]
        product_right = [1 for j in range(len(nums))]
        for i in range(1,len(nums)):
            product_left[i] = product_left[i-1]*nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            product_right[j] = product_right[j+1]*nums[j+1]
        res = [1 for i in range(0,len(nums))]
        for i in range(len(nums)):
            res[i] = product_left[i]*product_right[i]
        # print product_left,product_right
        return res

# # [0,0]
# # [1,0,1]