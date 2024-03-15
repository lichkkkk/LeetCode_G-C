# easy
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
      res = []
      for i in range(0, len(s), 2*k):
        res.append(s[i : min(i+k, len(s))][::-1])
        res.append(s[i+k : min(i+2*k, len(s))])
      return ''.join(res)
