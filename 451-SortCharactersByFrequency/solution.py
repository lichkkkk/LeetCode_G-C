from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
      counter = Counter(s)
      sorted_chars = sorted(counter.items(), key=lambda x: x[1], reverse=True)
      output = ''
      for char, cnt in sorted_chars:
        output += char * cnt
      return output
