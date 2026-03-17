class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past = {}
        for i, n in enumerate(nums):
            res = target - n
            if res in past:
                return [i, past[res]]
            else:
                past[n] = i
        raise Exception('no solution')
