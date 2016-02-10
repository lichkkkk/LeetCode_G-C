__author__ = 'liuxiyun'
# hashmap:
# TLE
# O(n^2)
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        word_map = []
        for word in words:
            word.lower()
            temp_map = [0]*26
            for letter in word:
                temp_map[ord(letter)-97]+=1
            word_map.append(temp_map)
        res = []
        i=0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                k = 0
                same = False
                for k in range(26):
                    if word_map[i][k]!=0 and word_map[j][k]!=0:
                        same = True
                        break
                if not same:
                    res.append(len(words[i])*len(words[j]))
        return 0 if res == [] else max(res)

# Same idea:
# Bit manipulation
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        word_map = []
        for word in words:
            word.lower()
            temp_map = 0
            for letter in word:
                temp_map|=1<<(ord(letter)-97)
            word_map.append(temp_map)
        res = []
        i=0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if word_map[i] & word_map[j] == 0:
                    res.append(len(words[i])*len(words[j]))
        return 0 if res == [] else max(res)