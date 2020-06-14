class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cc = Counter(chars)
        res = 0
        for w in words:
          wc = Counter(w)
          if all(wc[ch] <= cc[ch] for ch in w):
            res += len(w)
        return res
