__author__ = 'liuxiyun'

# We generate k-th string, and from k-th string we generate k+1-th string, until we generate n-th string.

# Use Two pointers to generate:
# Idea here is keep track of the first letter in the sequence and count consecutive occurances.
# Once you encounter a new letter you add the previous count and letter to the chain.
# Repeat n-1 times (since we seeded the initial '1' case).
# We always update temp after the inner loop since we will never have already added the last sequence.

# Time
# We'll have to calculate all the sequences s[1], s[1], ..., s[n - 1] before getting s[n].
# Thus the time complexity is O(len(s[1]) + len(s[2]) + ... + len(s[n -1])),
# the average rate of growth of s[i] is between (0, 2), thus the time complexity can be roughly O(2^n).

# Space complexity is O(2^n) too, as string buffer needs extra space

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        cur='1'
        if n==1:
            return cur
        for loop in range(1,n):
            i=0
            new=''
            while i<len(cur) and j<len(cur):
                j=i
                while j+1<len(cur) and cur[j]==cur[j+1]:
                    j=j+1
                length=j-i+1
                new=new+str(length)+cur[i]
                i=j+1
            cur=new
        return cur
