__author__ = 'liuxiyun'
# Be careful! The input is a list of char, not a string

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        i = 0
        while i<len(s):
            j = i
            while j< len(s) and s[j]!= " ":
                j+=1
            #s[i:j]need reverse
            x,y = i,j-1
            while x<y:
                s[x],s[y] = s[y],s[x]
                x+=1
                y-=1
            i=j+1
        i,j = 0,len(s)-1
        while i<j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1

# Assign the reversed part to the slice of list.

class Solution2(object):
    def reverseWords(self, s):
        """
        :type s: a list of 1 length strings (List[str])
        :rtype: nothing
        """
        i = 0
        while i<len(s):
            j = i
            while j< len(s) and s[j]!= " ":
                j+=1
            #s[i:j]need reverse
            s[i:j] = reversed(s[i:j])
            i=j+1
        i,j = 0,len(s)-1
        s.reverse()
        print s
c=Solution2()
print c.reverseWords(["a"," ", "b"])