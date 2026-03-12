class Solution:
    def removeOneDirection(self, s: str, p: str) -> str:
        res = ''
        left_cnt = 0
        for c in s:
            if c not in '()':
                res += c
            elif c == p:
                left_cnt += 1
                res += c
            elif left_cnt > 0:
                left_cnt -= 1
                res += c
        return res

    def minRemoveToMakeValid(self, s: str) -> str:
        s_tmp = self.removeOneDirection(s, '(')
        res_reversed = self.removeOneDirection(s_tmp[::-1], ')')
        return res_reversed[::-1]

    def minRemoveToMakeValid2(self, s: str) -> str:
        stack = []
        to_remove = set()
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop()
                else:
                    to_remove.add(i)
        to_remove |= set(stack)
        return ''.join(c for i, c in enumerate(s) if i not in to_remove)
