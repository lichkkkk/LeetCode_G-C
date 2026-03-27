class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        is_all_positive = all(n >= 0 for n in nums)
        is_all_non_positive = all(n <= 0 for n in nums)
        if is_all_positive or is_all_non_positive:
            res = heapq.nlargest(3, nums)
            return res[0] * res[1] * res[2]
        else:
            res_pos = heapq.nlargest(3, nums)
            res_neg = heapq.nsmallest(2, nums)
            if res_neg[0] * res_neg[1] > res_pos[1] * res_pos[2]:
                return res_neg[0] * res_neg[1] * res_pos[0]
            else:
                return res_pos[0] * res_pos[1] * res_pos[2]
