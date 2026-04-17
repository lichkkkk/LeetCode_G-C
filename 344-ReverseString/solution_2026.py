class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s)-1
        while l < r:
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp
            l, r = l + 1, r - 1
