class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_len = min([len(s) for s in strs])
        for i in range(max_len):
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
        return strs[0][:max_len]
