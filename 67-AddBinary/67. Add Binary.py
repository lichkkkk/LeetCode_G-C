__author__ = 'liuxiyun'

# Time: O(m+n)
# save the carry_bit, and add it

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res=''
        jinwei=0
        i,j = len(a)-1,len(b)-1
        while i>=0 and j>=0:
            new_num = int(a[i]) + int(b[j]) + jinwei
            jinwei = (new_num / 2)
            res += str(new_num % 2)
            i-=1
            j-=1
        if i < 0: # if a left
            while j>=0:
                new_num = int(b[j]) + jinwei
                jinwei = (new_num / 2)
                res += str(new_num % 2)
                j-=1
        if j < 0: # if b left
            while i>=0:
                new_num = int(a[i]) + jinwei
                jinwei = (new_num / 2)
                res += str(new_num % 2)
                i-=1
        if jinwei == 1: # if has carry_number
            res+=str(jinwei)
        return res[::-1]

# test case:
# # 0,0
# # 0,1
# # 1,1
# # 101,111
# # 11111111,11
# # 1000011,11