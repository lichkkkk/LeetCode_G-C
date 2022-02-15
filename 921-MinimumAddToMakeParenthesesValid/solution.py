class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0
        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                if len(stack) > 0:
                    stack.pop()
                else:
                    res += 1
        return res + len(stack)
