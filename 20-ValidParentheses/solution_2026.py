class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    pc = stack.pop()
                    if abs(ord(c) - ord(pc)) > 2:
                        return False
        return not stack
