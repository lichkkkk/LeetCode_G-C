class Solution:
    def longestPalindrome(self, s: str) -> str:
        table = [[True] * len(s) for _ in range(len(s))]
        start, end = 0, 0 # inclusive
        for i in range(len(s) - 1):
            table[i][i+1] = s[i] == s[i+1]
            if table[i][i+1]:
                start, end = i, i+1
        for diff in range(2, len(s)):
            for i in range(len(s) - diff):
                table[i][i+diff] = table[i+1][i+diff-1] and s[i] == s[i+diff]
                if table[i][i+diff]:
                    start, end = i, i+diff
        return s[start:end+1]
