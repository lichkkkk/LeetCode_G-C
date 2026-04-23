class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # can be optimized with rolling window bit manipulation
        cnt = Counter()
        for i in range(len(s) - 9):
            cnt[s[i:i+10]] += 1
        return [k for k, v in cnt.items() if v > 1]
 
