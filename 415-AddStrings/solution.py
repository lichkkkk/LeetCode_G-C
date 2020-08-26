class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num2 = '0'*(len(num1)-len(num2)) + num2
        else:
            num1 = '0'*(len(num2)-len(num1)) + num1
        carry = 0
        res= []
        for i in range(len(num1)-1, -1, -1):
            s = int(num1[i]) + int (num2[i]) + carry
            carry = s // 10
            res.append(str(s % 10))
        if carry:
            res.append('1')
        return "".join(reversed(res))
