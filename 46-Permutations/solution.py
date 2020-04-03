"""
46. Permutations
licha@London, Apr. 3rd, 2020
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums_left = set(nums)
        all_res = []
        self.helper(nums_left, [], all_res)
        return all_res
    
    def helper(self, nums_left, curr_res, all_res):
        if len(nums_left) == 0:
            all_res.append(curr_res.copy())
            return
        for num in list(nums_left):
            nums_left.remove(num)
            curr_res.append(num)
            self.helper(nums_left, curr_res, all_res)
            curr_res.pop()
            nums_left.add(num)
