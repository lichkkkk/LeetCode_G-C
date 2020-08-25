class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for i, j in enumerate(indices):
            res[j] = s[i]
        return "".join(res)
