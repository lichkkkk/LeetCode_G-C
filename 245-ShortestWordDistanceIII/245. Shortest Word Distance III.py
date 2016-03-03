__author__ = 'liuxiyun'
# Just try use zip.
# Actually can do it one pass.
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        min_dis = 27000000
        if word1 == word2:
            idx = [i for i,word in enumerate(words) if word == word1]
            min_dis = [y - x for x,y in zip(idx,idx[1:])]
            return min(min_dis)

        idx1,idx2 = -2700000,-2700000
        for i,word in enumerate(words):
            if word == word1:
                idx1=i
            elif word == word2:
                idx2=i
            else:
                continue
            min_dis = min(min_dis,idx2-idx1)
        return min_dis
