__author__ = 'liuxiyun'

# (continuous subarray)
# Since the given array contains only positive integers, the subarray sum can only increase by including more elements.
# Therefore, you don't have to include more elements once the current subarray already has a sum large enough.
# My idea is:  Two pointers
# if sum >= s: move left pointer a step right, else: move right pointer a step right. update the sum
# Time: O(n)
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        if len(nums)==1:
            return 1 if s<nums[0] else 0
        nums_len = len(nums)
        i,j = 0,0
        sums = nums[i]
        min_len = nums_len
        get_it = False
        while i<nums_len and j<nums_len and i<=j:
            # print nums[i:j+1], sums
            if sums >= s:
                min_len = min(min_len,j-i+1)
                sums -= nums[i]
                i+=1
                get_it = True
            else:
                if j+1 < nums_len:
                    sums += nums[j+1]
                j+=1
        return min_len if get_it == True else 0

#As to NLogN solution, logN immediately reminds you of binary search.
# In this case, you cannot sort as the current order actually matters. How does one get an ordered array then?
# Since all elements are positive, the cumulative sum must be strictly increasing.
# Then, a subarray sum can expressed as the difference between two cumulative sum.
#  Hence, given a start index for the cumulative sum array, the other end index can be searched using binary search.

    def nLogN(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sums=[0 for i in range(len(nums)+1)]
        for i in range(1,len(nums)+1):
            sums[i] = nums[i-1] + sums[i-1] # sum from start
        min_len = len(nums) + 1
        print sums
        for i in range(0, len(nums)):
            end = self.binarysearch(i+1,len(sums)-1,sums, s+sums[i] ,nums)
            if end == len(sums):
                break
            print nums[i:end]
            min_len = min(min_len,end-i)
        return min_len if min_len!=len(nums)+1 else 0
    def binarysearch(self,low,high,sums, target, nums):
        while low<=high:
            mid = (low+high)/2
            if sums[mid] == target:
                return mid
            elif sums[mid]<target:
                low = mid +1
            else:
                high = mid -1
        return low


# Test case:
# # 6 [10,2,3] : 1
# # 3 [1,1] : 0
# # 11 [1,2,3,4,5] : 3