class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        while i * 2 + 1 < len(s):
            if s[i] != s[len(s)-i-1]:
                return self.helper(s[i+1:len(s)-i]) or self.helper(s[i:len(s)-i-1])
            i += 1
        return True

    def helper(self, s: str) -> bool:
        i = 0
        while i * 2 + 1 < len(s):
            if s[i] != s[len(s)-i-1]:
                return False
            i += 1
        return True
