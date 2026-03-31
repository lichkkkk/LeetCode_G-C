from collections import Counter

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1, c2 = Counter(words1), Counter(words2)
        once1 = set([k for k, v in c1.items() if v == 1])
        once2 = set([k for k, v in c2.items() if v == 1])
        return len(once1 & once2)
 
