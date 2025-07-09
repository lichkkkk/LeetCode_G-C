class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        char_seen = set()
        for c in s:
            if c in char_seen:
                char_seen.remove(c)
                res += 2
            else:
                char_seen.add(c)
        return min(res + 1, len(s))
