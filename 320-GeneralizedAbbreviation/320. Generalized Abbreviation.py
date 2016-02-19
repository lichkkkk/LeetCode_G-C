__author__ = 'liuxiyun'
# Backtracking
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        self.res = []
        self.helper("",0,word)
        return self.res

    def helper(self,temp,start,word):
        if start >= len(word):
            self.res.append(temp[:])
            return
        self.res.append(temp+word[start:])# if ab_len = 0, means no abbreviation later
        for ab_len in range(1,len(word)-start+1): # if need abbreviation
            for i in range(start,len(word)-ab_len+1):
                temp_temp = temp
                temp = temp+word[start:i]+str(ab_len)
                if i+ab_len<len(word):
                    temp+=word[i+ab_len]
                self.helper(temp,i+ab_len+1,word)
                temp = temp_temp

# First make string contains 1 and 0, 1 means this letter need to be abb, 0 means not
# Then use 10 string to generate abb
class Solution10(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        self.list_10 = []
        self.word_len = len(word)
        self.one_zero("")
        self.word = word
        # print self.list_10
        self.res = []
        self.make_abb()
        return self.res

    def one_zero(self,temp):
        if len(temp)==self.word_len:
            self.list_10.append(temp)
            return
        for i in range(0,2):
            self.one_zero(temp+str(i))

    def make_abb(self):
        for choice in self.list_10:
            i=0
            temp = ""
            # print choice
            while i<self.word_len:
                if choice[i] == "0":
                    temp+=self.word[i]
                    i+=1
                else:
                    j=i+1
                    while j<self.word_len and choice[j]=="1":
                        j+=1
                    temp+=str(j-i)
                    i=j
            self.res.append(temp)
# Wrong
# Need modify
class Solution1(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        self.res = []
        self.helper(0,word)
        return self.res
    def helper(self,start,word):
        self.res.append(word[:])
        # if 0 == len(word):
        #     return
        for ab_len in range(1,len(word)-start+1):
            for i in range(start,len(word)-start+1-ab_len):
                # temp = temp[:i]+str(ab_len)+temp[i+ab_len:]
                self.helper(i+ab_len+1,word[:i]+str(ab_len)+word[i+ab_len:])
                # temp = temp_temp
c = Solution()
print c.generateAbbreviations("word")

