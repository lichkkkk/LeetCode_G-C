class Solution(object):
    def palindromePairs(self, words):
        def isPal(s):
            for i in xrange(len(s)/2):
                if s[i] != s[len(s)-1-i]:
                    return False
            return True
        wmap = {word : index for index, word in enumerate(words)}
        res = [];
        for idx, word in enumerate(words):
            if word != "" and isPal(word) and "" in wmap:
                res.append((wmap[""], idx))
            for i in xrange(len(word)):
                left, right = word[:i], word[i:]
                rl, rr = left[::-1], right[::-1]
                if isPal(right) and rl in wmap and wmap[rl] != idx:
                    res.append((idx, wmap[rl]))
                if isPal(left) and rr in wmap and wmap[rr] != idx:
                    res.append((wmap[rr], idx))
        return res            