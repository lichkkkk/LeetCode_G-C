class Solution:
    def calculateScore(self, s: str) -> int:
        score = 0
        char_pos = {c: [] for c in range(26)}
        for i in range(len(s)):
          curr = ord(s[i]) - ord('a')
          mirror = 25 - curr
          bank = char_pos[mirror]
          if not bank:
            char_pos[curr].append(i)
          else:
            j = bank.pop(-1)
            score += i - j
        return score
