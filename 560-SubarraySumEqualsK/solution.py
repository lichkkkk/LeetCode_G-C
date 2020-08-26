class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        table = {}
        curr_sum = total = sum(nums)
        for i in range(len(nums)):
            if curr_sum not in table:
                table[curr_sum] = []
            table[curr_sum].append(i)
            curr_sum -= nums[i]
        if 0 not in table:
            table[0] = []
        table[0].append(len(nums))
        res = 0
        l_sum = 0
        for i in range(len(nums)):
            target_r_sum = total - k - l_sum
            if target_r_sum in table:
                # can use binary search
                res += sum(idx > i for idx in table[target_r_sum])
            l_sum += nums[i]
        return res
