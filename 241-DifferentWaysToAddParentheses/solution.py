class Solution:
    
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y
    }
        
    def diffWaysToCompute(self, input: str) -> List[int]:
        return self.helper(input, {})
    
    def helper(self, s, cache):
        if s in cache:
            return cache[s]
        res  = []
        for i in range(len(s)):
            if s[i] in ('+', '-', '*'):
                lres = self.helper(s[:i], cache)
                rres = self.helper(s[i+1:], cache)
                res.extend(self.merge(s[i], lres, rres))
        if len(res) == 0:
            res.append(int(s))
        cache[s] = res
        return res
    
    def merge(self, ch, lres, rres):
        res = []
        for l in lres:
            for r in rres:
                res.append(self.ops[ch](l, r))
        return res
