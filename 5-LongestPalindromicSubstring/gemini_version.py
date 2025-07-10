class Solution:

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        # dp[i][j] is True if the substring s[i..j] is a palindrome
        dp = [[False] * n for _ in range(n)]

        start = 0
        max_len = 1

        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True

        # Check for substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_len = 2

        # Check for substrings of length 3 or more
        # k is the length of the substring
        for k in range(3, n + 1):
            # i is the starting index
            for i in range(n - k + 1):
                # j is the ending index
                j = i + k - 1
                
                # A substring is a palindrome if:
                # 1. The outer characters match (s[i] == s[j])
                # 2. The inner substring is also a palindrome (dp[i+1][j-1])
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    # If we found a longer palindrome, update the result
                    if k > max_len:
                        start = i
                        max_len = k
                        
        return s[start : start + max_len]
