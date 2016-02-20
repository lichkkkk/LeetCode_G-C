__author__ = 'liuxiyun'
# Time: O(5^n)
#Iterative (faster than recursive)
class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        poss = "01689"
        dic = ["0",'1','0','0','0','0','9','0','8','6']
        if n%2 == 0:
            res = ['']
            nn = 0
        else:
            res = ['0','1','8']
            nn = 1
        temp = res
        while nn<n:
            res = []
            for i in range(5):
                if nn == n-2 and i == 0:
                    continue
                for add in temp:
                    res.append(poss[i]+add+dic[int(poss[i])])
            temp = res
            nn += 2
        return temp

# Recursive, super slow
class Solution2(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ['0','1','8']
        poss = "01689"
        self.dic = ["0",'1','0','0','0','0','9','0','8','6']
        self.res = []
        self.n = n
        return self.combination(n,poss)
    def combination(self,n,poss):
        if n==0:
            return ['']
        if n == 1:
            return ['0','1','8']
        res = []
        for i in range(5):
            if self.n == n and i == 0:
                continue
            temp = self.combination(n-2,poss)
            for add in temp:
                res.append(poss[i]+add+self.dic[int(poss[i])])
        return res

# Insert the candidate into the middle of the previous possible string.
# Fast, from discuss
class Solution3(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        evenMidCandidate = ["11","69","88","96", "00"]
        oddMidCandidate = ["0", "1", "8"]
        if n == 1:
            return oddMidCandidate
        if n == 2:
            return evenMidCandidate[:-1]
        if n % 2:
            pre, midCandidate = self.findStrobogrammatic(n-1), oddMidCandidate
        else:
            pre, midCandidate = self.findStrobogrammatic(n-2), evenMidCandidate
        premid = (n-1)/2
        return [p[:premid] + c + p[premid:] for c in midCandidate for p in pre]
c=Solution()
c.findStrobogrammatic(2)