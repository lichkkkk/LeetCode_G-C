__author__ = 'liuxiyun'
# O(n^2)
# Sort the list
# --> two sum smaller
# Two pointers, set left pointer on the left, move right pointer, if smaller, count+len(s[j:k+1])
# Then move left pointer one step right

class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)<=2:
            return 0
        count = 0
        nums.sort()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                temp_sum = nums[j]+nums[k]
                if temp_sum>=target-nums[i]:
                    k-=1
                else:
                    count += (k-j)
                    j+=1
        return count