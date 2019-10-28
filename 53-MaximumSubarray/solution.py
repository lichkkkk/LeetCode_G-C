class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best_so_far = nums[0]
        curr_sum = 0
        for n in nums:
            curr_sum += n
            best_so_far = max(best_so_far, curr_sum)
            curr_sum = max(0, curr_sum)
        return best_so_far
