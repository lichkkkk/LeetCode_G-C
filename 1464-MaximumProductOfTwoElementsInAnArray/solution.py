class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def update(i, j, k):
            if nums[i] <= nums[j] and nums[i] <= nums[k]:
                return j, k
            elif nums[j] <= nums[i] and nums[j] <= nums[k]:
                return i, k
            else:
                return i, j
        
        i1, i2 = 0, 1
        for i in range(2, len(nums)):
            i1, i2 = update(i, i1, i2)
        
        return (nums[i1] - 1) * (nums[i2] - 1)
