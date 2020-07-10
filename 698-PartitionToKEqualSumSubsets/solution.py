class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums_sum = sum(nums)
        target = nums_sum // k
        if target * k != nums_sum:
            return False
        curr_state = [0] * k
        return self.place(sorted(nums, reverse=True), 0, target, curr_state)
        
    def place(self, nums, next_pos, target, curr_state):
        if next_pos == len(nums):
            return True
        for i in range(len(curr_state)):
            curr_state[i] += nums[next_pos]
            if curr_state[i] <= target and self.place(nums, next_pos+1, target, curr_state):
                return True
            curr_state[i] -= nums[next_pos]
            # If this is True, that means currently no number is put for pos > i
            # since it's the same to put a number on any empty bucket, so we can break
            if curr_state[i] == 0:
                break
        return False
