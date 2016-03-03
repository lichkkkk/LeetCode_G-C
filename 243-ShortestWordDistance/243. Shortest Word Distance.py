__author__ = 'liuxiyun'
# Save word1 and word2's index. update min_dis if necessary
# O(n) time
# O(1) space
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        min_dis = 27000000
        idx1 = -1
        idx2 = -1
        for i,word in enumerate(words):
            if word == word1:
                idx1=i
                if idx2!=-1:
                    min_dis = min(min_dis,idx1-idx2)
            elif word == word2:
                idx2=i
                if idx1!=-1:
                    min_dis = min(min_dis,idx2-idx1)
        return min_dis

