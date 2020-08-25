class Solution:
    def numSub(self, s: str) -> int:
        return sum(len(subs) * (len(subs)+1) // 2 for subs in s.split("0")) % (10**9 + 7)
