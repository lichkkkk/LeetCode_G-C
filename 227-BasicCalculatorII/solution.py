"""
A cleaner solution by others:
https://leetcode.com/problems/basic-calculator-ii/discuss/63076/Python-short-solution-with-stack.
"""
class Solution:
    ops = '+-*/'
    nums = '0123456789'
    
    def calculate(self, s: str) -> int:
        stack = []
        index = 0
        while True:
            # read one op and one number, like '+' and '123'
            sym, index = self.getNextSymbol(s, index)
            if not sym:
                break
            if sym not in self.ops:
                op = '+'
                num = int(sym)
            else:
                op = sym
                sym, index = self.getNextSymbol(s, index)
                num = int(sym)
            # handle the op-num pair
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-1 * num)
            elif op == '*':
                stack[-1] = stack[-1] * num
            else:
                stack[-1] = (1 if stack[-1] > 0 else -1)  * (abs(stack[-1]) // num)
        return sum(stack)
  
    def getNextSymbol(self, s, start):
        while start < len(s) and s[start] == ' ':
            start += 1
        if start == len(s):
            return (None, start)
        if s[start] in self.ops:
            return (s[start], start+1)
        end = start + 1
        while end < len(s) and s[end] in self.nums:
            end += 1
        return (s[start:end], end)
