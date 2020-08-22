class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = sorted([(sum(mat[i]), i) for i in range(len(mat))])
        return [res[i][1] for i in range(k)]
    
    # we can replace sum above with this binary search function
    def countOnes(self, nums):
        if nums[0] == 0:
            return 0
        if nums[-1] == 1:
            return len(nums)
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] == 0:
                r = mid
            else:
                l = mid
        return l + 1
