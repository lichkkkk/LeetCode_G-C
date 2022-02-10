class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        cnt = 0
        # Step 1: push in stack and remove redundant right parenteses
        for ch in s:
            if ch == '(':
                stack.append(ch)
                cnt += 1
            elif ch == ')':
                if cnt > 0:
                    cnt -= 1
                    stack.append(ch)
                else:
                    pass
            else:
                stack.append(ch)
        # Step 2: remove redundant left parenteses in reversed order
        i = len(stack) - 1
        while cnt > 0 and i >= 0:
            if stack[i] == '(':
                stack[i] = ''
                cnt -= 1
            i -= 1
        return ''.join(stack)
