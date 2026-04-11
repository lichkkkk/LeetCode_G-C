class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        to_insert, curr = 1, 1
        while curr < len(nums):
            if nums[curr] != nums[curr-1]:
                nums[to_insert] = nums[curr]
                to_insert += 1
            curr += 1
        return to_insert
 
