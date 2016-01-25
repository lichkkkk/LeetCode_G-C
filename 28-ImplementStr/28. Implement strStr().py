__author__ = 'liuxiyun'
# broot force:
# Check each element in naystack whether it is the start of the needle and the following len(needle) letter is equal to needle


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        if haystack == '':
            return -1
        hay_len = len(haystack)
        nee_len = len(needle)
        for i in range(hay_len - nee_len + 1):
            if haystack[i:i+nee_len] == needle:
                return i
        return -1

# Test case:
# # '', ''
# # "a", "a"
# # "abcd", 'bc'
# # 'abcd', 'd'