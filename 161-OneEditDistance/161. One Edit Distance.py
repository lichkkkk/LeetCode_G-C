__author__ = 'liuxiyun'

# Idea:
# Basically just go through the two string, if encounter that two letters doesn't match,
# check if should move to the next digit or they reach the end, or return False
# Then check if the distance == 1

# Time complexity: Go through the whole two string. O(len(s)+len(t))
class Solution(object):
    def isOneEditDistance(self, s, t): # check if the distance is 1
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i,j = 0,0
        distance = 0
        len1, len2=len(s), len(t)
        while i<len1 and j<len2:
            if s[i]==t[j]:
                i += 1
                j += 1
            else:
                if j < len2 - 1 and s[i] == t[j+1]:
                    j+=1
                elif i < len1 - 1 and s[i+1] ==t[j]:
                    i+=1
                elif i < len1 - 1 and j != len2 - 1 and s[i+1]==t[j+1] or (i == len1-1 and j == len2-1):
                    i+=1
                    j+=1
                else:
                    return False
                distance+=1
        distance += max(len1-i,len2-j)
        return True if distance == 1 else False

# Follow up:
# # Edit distance // dp
    def EditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len1=len(s)
        len2=len(t)
        # initialize
        if s=='' or t=='':
            return True if max(len1,len2)<=1 else False
        distance=[[0 for j in range(len2)] for i in range(len1)]
        for i in range(0,len1):
            distance[i][0]=i
        for j in range(0,len2):
            distance[0][j]=j
        print distance
        for i in range(0,len1):
            for j in range(0,len2):
                if s[i]==t[j]:
                    distance[i][j]=distance[i-1][j-1]
                else:
                    distance[i][j]=distance[i-1][j-1]+1
                distance[i][j] = min(distance[i][j],distance[i][j-1]+1,distance[i-1][j]+1)
        print distance
        return distance[len1-1][len2-1]



#Test case:
# # '','' //empty
# # '','a' // one is empty
# # '','ab'
# # 'a', 'A'
# # 'a','ab'
# # 'abc','abdc'
# # 'abc','abd'
# # 'abc','ab'
# # 'abc','actr'