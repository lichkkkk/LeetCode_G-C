class Solution:
    def customSortString(self, S: str, T: str) -> str:
        keys = [26] * 26;
        for i in range(len(S)):
            keys[ord(S[i]) - ord('a')] = i
        return "".join(sorted(T, key=lambda ch : keys[ord(ch) - ord('a')]))
    
    def customSortString2(self, S: str, T: str) -> str:
        cnt = Counter(T)
        res = []
        for ch in S:
            if ch in cnt:
                res.append(ch * cnt.pop(ch))
        for ch in cnt:
            res.append(ch * cnt[ch])
        return "".join(res)
