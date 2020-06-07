class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
      return self.helper(s, t, 0, 0, {})
    
    def helper(self, s, t, s_idx, t_idx, cache):
      if s_idx == len(s):
        return True
      if len(t) - t_idx < len(s) - s_idx:
        return False
      if (s_idx, t_idx) in cache:
        return cache[(s_idx, t_idx)]
      if s[s_idx] == t[t_idx]:
        res = self.helper(s, t, s_idx + 1, t_idx + 1, cache)
      else:
        res = self.helper(s, t, s_idx, t_idx + 1, cache)
      cache[(s_idx, t_idx)] = res
      return res
