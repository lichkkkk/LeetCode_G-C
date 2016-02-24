__author__ = 'liuxiyun'
# That is life

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = '('+s+')'
        stack = []
        i = 0
        while i<len(s):
            ele = s[i]
            if ele == ')':
                # print "meet )"
                equation = []
                start = stack.pop()
                while stack and start!='(':
                    print stack
                    equation.append(start)
                    start=stack.pop()

                equation.reverse()
                temp = self.helper(equation)
                stack.append(temp)
                i+=1
            elif ele == ' ':
                i+=1
                continue
            elif ele in '(+-':
                stack.append(ele)
                i+=1
                # print "stack append:",ele
            else:
                j = i
                while j<len(s) and s[j] not in "+-()":
                    j+=1
                stack.append(s[i:j])
                i=j

        return int(stack[0])

    def helper(self,equation):
        res = int(equation[0])
        i = 1
        while i<len(equation):
            if equation[i] == '+':
                res+=int(equation[i+1])
            else:
                res-=int(equation[i+1])
            i+=2
        return str(res)
c = Solution()
print c.calculate('1+2')
print c.helper(['1','+','2'])