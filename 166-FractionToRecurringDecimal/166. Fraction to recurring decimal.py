__author__ = 'liuxiyun'
# Edge case: negative, 0
# Use hashmap to save the numerator. If meet a same one, we know that there is a cycle
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = ''
        if ((numerator>0) ^ (denominator>0)) and numerator!=0:
            res+='-'
        a,b = abs(int(numerator)),abs(int(denominator))
        res+=str(a/b)
        if a%b == 0:
            return res
        else:
            res+='.'
            a = a%b
        pre = 0
        dic = {a:len(res)}
        while a!=0:
            a = 10*a
            res+=str(a/b)
            a = a%b
            if a in dic:
                res = res[:dic[a]]+'('+res[dic[a]:]+')'
                break
            else:
                dic[a]=len(res)
        return res