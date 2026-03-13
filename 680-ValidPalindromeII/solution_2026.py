class Solution:
    # # recursion is much slower
    # def valid(self, s: str) -> bool:
    #     if len(s) <= 1: return True
    #     if s[0] != s[-1]: return False
    #     return self.valid(s[1:-1])

    # def validPalindrome(self, s: str) -> bool:
    #     if len(s) <= 2: return True
    #     if s[0] == s[-1]: return self.validPalindrome(s[1:-1])
    #     else: return self.valid(s[1:]) or self.valid(s[:-1])

    def valid(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while right > left:
            if s[left] != s[right]: return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while right > left:
            if s[left] != s[right]:
                return self.valid(s[left+1:right+1]) or self.valid(s[left:right])
            else:
                left += 1
                right -= 1
        return True
