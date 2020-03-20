"""
    Key Points:
        Let's consider a simpler example: [a, b, c]. It has many sub arraries: [a],
        [a, b], [a, b, c], [b, c], etc. Let's assume a < 0, then it's obvious the
        max subarry will not contain a. Because not matter it's [a, b] or [a, b, c],
        removing a will only make it larger. Similarly, if a + b < 0, then [c] itself
        is definitely larger than [a, b, c].
        So, the key point here is, we scan from left to right and memorizing the sum
        so far, once it's < 0, we just completely ignore all previous elements in the
        array, like they never exist. Since no matter what the following elements are,
        they will be larger without the previous elements.
        Of course, the sum may be > 0 first, then we see a large negative number and
        the sum becomes negative. In order not to miss the positive result we ever had,
        we use a global variable to track the max sum ever appearred.
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        best_so_far = nums[0] # initialize it with the first element. If the array only has one element, then it's the answer
        curr_sum = 0 # the sum of previous elements that we have not discarded
        for n in nums: # scan from left to right
            curr_sum += n # current sum, if all previous elements are discarded(i.e. curr_sum=0), then it's n itself
            best_so_far = max(best_so_far, curr_sum) # update max sum we have seen so far
            curr_sum = max(0, curr_sum) # if curr_sum < 0, we just discard all previous elements by resetting it as 0
        return best_so_far
