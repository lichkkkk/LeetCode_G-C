__author__ = 'liuxiyun'
# O(n)
# Using stack to save the current result. Pop the last element if the new letter need to be added before the last element
# Added the current letter into stack anyway.
from collections import defaultdict
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        dic = defaultdict(int)
        added = defaultdict(bool) # if the letter is in the current result
        for letter in s:
            dic[letter]+=1

        for l in s:
            if added[l]: # if the letter is in the current result, pass
                dic[l]-=1 # This is because if the letter's position need to be change, it have already been changed before and no need to check again.
                continue
            while stack!=[] and dic[stack[-1]]!=0 and l<stack[-1]: # if should move forward
                pre = stack.pop() # pop the previous letter which will be added later
                added[pre] = False
            stack.append(l)
            added[l]=True
            dic[l]-=1
        return "".join(x for x in stack)