__author__ = 'liuxiyun'
from collections import defaultdict
class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.dic = defaultdict(list)
        for i,word in enumerate(words):
            self.dic[word].append(i)

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        return min([abs(x-y) for x in self.dic[word1] for y in self.dic[word2]])


# Your WordDistance object will be instantiated and called as such:
c = WordDistance(["practice", "makes", "perfect", "coding", "makes"])
print c.shortest('coding','practice')
print c.shortest("makes", "coding")