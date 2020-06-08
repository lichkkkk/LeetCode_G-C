class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
      return self.helper(text1, text2, 0, 0, {})
        
    def helper(self, text1, text2, idx1, idx2, cache):
      if len(text1) == idx1 or len(text2) == idx2:
        return 0
      elif (idx1, idx2) in cache:
        return cache[(idx1, idx2)]
      else:
        if text1[idx1] == text2[idx2]:
          res = self.helper(text1, text2, idx1 + 1, idx2 + 1, cache) + 1
        else:
          res = max(self.helper(text1, text2, idx1, idx2 + 1, cache),
                    self.helper(text1, text2, idx1 + 1, idx2, cache))
        cache[(idx1, idx2)] = res
        return res
