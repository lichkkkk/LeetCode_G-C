class Solution:
    def f(self, nums: list[int], i: int, j: int, cache: dict[Any, int]) -> int:
        cache_key = (i, j)
        if cache_key in cache:
            return cache[cache_key]
        if i + 2 > len(nums):
            return max(nums[i:] + [j])
        # can be further optimized since there is no reason to keep the mid num
        res = min([
            self.f(nums, i+2, j, cache) + max(nums[i:i+2]),
            self.f(nums, i+2, nums[i], cache) + max(nums[i+1], j),
            self.f(nums, i+2, nums[i+1], cache) + max(nums[i], j),
        ])
        cache[cache_key] = res
        return res

    def minCost(self, nums: List[int]) -> int:
        '''
        the smaller one is removed for free -- that's what we are trying to optimize
        is greedy the global optimal?
         -- [1, 2, 9, 8] -> you should not remove 9 at the first time, so no
         DP -> every time you have 3 options, you find the best out of those 3
         ->there are total 3 * N sub problems

        i = the index to start, j = the previous left over number
        f(i, j) = the min cost for state i, j
        res = f(i=1, j=nums[0])
        f(i, j) = min(
            f(i+2, j) + max(nums[i:i+2])
            f(i+2, nums[i]) + max(...)
            f(i+2, nums[i+1]) + max(...)
        )
        boundary condition:
            if i + 2 > len(nums): f(i, j) = max(num[i:] + [j])
        Maybe easier to just use {} to cache state instead of table filling
        '''
        return self.f(nums, 1, nums[0], {})
