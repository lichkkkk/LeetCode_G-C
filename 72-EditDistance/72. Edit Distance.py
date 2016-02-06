__author__ = 'liuxiyun'
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == "" and word2 == "":
            return 0
        if word1 == "":
            return len(word2)
        if word2 == "":
            return len(word1)
        table = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        for i in range(1,len(word1)+1):
            table[i][0] = table[i-1][0] + 1
        for j in range(1,len(word2)+1):
            table[0][j] = table[0][j-1] + 1

        for i in range(0,len(word1)):
            for j in range(0,len(word2)):
                if word1[i] == word2[j]:
                    add = 0
                else:
                    add = 1
                table[i+1][j+1] = min(table[i][j+1]+1,table[i+1][j]+1,table[i][j]+add)
        return table[-1][-1] # be careful about what should return