class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            n = nums[i] - 1
            while nums[n] != 0:
                tmp = nums[n] - 1
                nums[n] = 0
                n = tmp
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]
