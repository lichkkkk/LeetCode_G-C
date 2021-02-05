class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        failure_cache = [set() for i in range(len(nums))]
        return self.helper(nums, 0, sum(nums), 0, failure_cache)
    
    def helper(self, nums, idx, rest_sum, diff, failure_cache):
        if idx == len(nums):
            return diff == 0
        if diff in failure_cache[idx] or \
                abs(rest_sum) < abs(diff) or \
                (abs(rest_sum) + abs(diff)) % 2 == 1:
            return False
        n = nums[idx]
        rest_sum -= n
        res = self.helper(nums, idx+1, rest_sum, diff+n, failure_cache) or \
                self.helper(nums, idx+1, rest_sum, diff-n, failure_cache)
        if not res:
            failure_cache[idx].add(diff)
        return res
