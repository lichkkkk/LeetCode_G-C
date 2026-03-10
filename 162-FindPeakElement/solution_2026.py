class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        print(nums)
        if len(nums) == 1: return 0
        if nums[1] < nums[0]: return 0
        if nums[-2] < nums[-1]: return len(nums) - 1
        # need to bisect
        assert len(nums) > 2
        mid = len(nums) // 2
        if nums[mid-1] < nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid-1] > nums[mid] > nums[mid+1]:
            return self.findPeakElement(nums[:mid])
        else:
            return self.findPeakElement(nums[mid:]) + mid
