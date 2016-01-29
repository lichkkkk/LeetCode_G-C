__author__ = 'liuxiyun'

# like quick sort
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k=len(nums)-k+1
        return self.helper(nums,k)
    def helper(self,nums,k):
        if len(nums)==1:
            return nums[0]
        star = random.randrange(0,len(nums))
        small = []
        good = []
        large = []
        for num in nums:
            if num< nums[star]:
                small.append(num)
            elif num == nums[star]:
                good.append(num)
            else:
                large.append(num)
        if k<=len(small):
            return self.helper(small,k)
        if len(small) < k <= len(small)+len(good):
            return good[0]
        if len(small)+len(good) < k:
            return self.helper(large,k-len(small)-len(good))

#Quick sort
def sort(array=[12,4,5,6,7,3,1,15]):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

