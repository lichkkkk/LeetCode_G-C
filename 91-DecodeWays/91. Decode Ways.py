__author__ = 'liuxiyun'
# DP
# #dp[i] = dp[i-1] if s[i-1] != "0
#       +dp[i-2] if "09" < s[i-2:i] < "27"
# O(n)
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "": return 0
        if s == '0': return 0
        num_ways = [0 for i in range(len(s)+1)] # num_ways[i+1] save # of ways end in s[i]
        num_ways[0]=1
        for i in range(0,len(s)):
            if s[i] != "0":
                num_ways[i+1] = num_ways[i] # ways of s[i] = ways of s[i-1]
            if i != 0 and int(s[i-1]+s[i]) in range(10,27): # 01 ways is 0
                num_ways[i+1]+=num_ways[i+1-2] # ways of s[i] += ways of s[i-2]
        return num_ways[-1]

# Brute force
    def numDecodings2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0
        self.res = []
        temp=[]
        self.helper(temp,0,s)
        # count = 0
        print self.res
        # for way in self.res:
        #     if self.valid(way):
        #         count +=1
        print len(self.res)
        return len(self.res)

    def helper(self,temp,i,s):
        if i==len(s):
            self.res.append(temp[:])
        if i<len(s):
            temp.append(s[i])
            self.helper(temp,i+1,s)
            temp.pop()
        if i<len(s)-1 and int(s[i]+s[i+1]) in range(1,27):
            temp.append(s[i]+s[i+1])
            self.helper(temp,i+2,s)
            temp.pop()
c=Solution()
"10"
"0"
"1234"
"0123"
