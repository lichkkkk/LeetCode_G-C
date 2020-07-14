class Solution:
    def numDecodings(self, s: str) -> int:
        nums = [9, 9] + [ord(ch) - ord('0') for ch in s]
        table = [0] * len(nums)
        table[0] = table[1] = 1
        for i in range(2, len(table)):
            if nums[i] != 0:
                table[i] += table[i-1]
            if nums[i-1] != 0 and 0 < nums[i-1] * 10 + nums[i] < 27:
                table[i] += table[i-2]
            if table[i] == 0:
                return 0
        return table[-1]
