class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        l, r = start, start
        while True:
            if nums[l] == target:
                return start - l
            if nums[r] == target:
                return r - start
            if l > 0:
                l -= 1
            if r < len(nums) - 1:
                r += 1
