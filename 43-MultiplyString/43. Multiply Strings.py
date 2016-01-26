__author__ = 'liuxiyun'

# Just .... multipy manually....
# the tricky way is " return str(int(num1)*int(num)2)" and it super fast = =
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1=len(num1)
        len2=len(num2)
        sum = 0
        for i in range(len1-1,-1,-1):
            tempsum = 0
            for j in range(len2-1,-1,-1):
                tempsum+=int(num2[j])*int(num1[i])*(10**(len2-j-1))
            sum += tempsum*(10**(len1-i-1))
        return str(sum)

c=Solution()
# # '0' '0'
# # '888' '2'
# # '100' '3'
# # '888' '29'