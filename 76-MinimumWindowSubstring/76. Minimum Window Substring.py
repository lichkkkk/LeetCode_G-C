__author__ = 'liuxiyun'
#1. Use two pointers: start and end to represent a window.
# 2. Move end to find a valid window.
# 3. When a valid window is found, move start to find a smaller window.
# To check if a window is valid, we use a dic(hashmap) to store (char, count) for chars in t.
# And use counter for the number of chars of t to be found in s.
#  The key part is dic[s[end]]--;.
# We decrease count for each char in s. If it does not exist in t, the count will be negative.
# O(n)

from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = defaultdict(int)
        for letter in t:
            dic[letter]+=1

        start,min_len = 0,len(s)+1
        i,j = 0,0
        count = len(t)
        if s[i] in dic:
            dic[s[i]]-=1
            count -=1
        while i<=j and j<len(s):
            if count == 0:
                if j-i+1 < min_len:
                    start = i
                    min_len = j-i+1
                if s[i] in t:
                    if dic[s[i]]>=0:
                        count +=1
                    dic[s[i]]+=1
                i+=1
            else:
                j+=1
                if j<len(s) and s[j] in t:
                    if dic[s[j]]>0:
                        count-=1
                    dic[s[j]]-=1
        return s[start:start+min_len] if min_len<len(s)+1 else ""

# Test case:
# # "aa", "aa"
# # 'a', 'a'
c=Solution()
# print c.minWindow("bbaa","aba")
print c.minWindow("abcdabcd","acd")
