class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match_map = {'(': ')', '[': ']', '{': '}'}
        for ch in s:
            if ch in match_map:
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                last_in = stack.pop()
                if ch != match_map[last_in]:
                    return False
        return len(stack) == 0
