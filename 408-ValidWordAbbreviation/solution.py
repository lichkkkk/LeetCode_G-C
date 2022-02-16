class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(abbr):
            if abbr[i] == '0':
                return False
            seg = abbr[i]
            while i + 1 < len(abbr) and abbr[i].isdigit() == abbr[i+1].isdigit():
                i += 1
                seg += abbr[i]
            i += 1
            if not seg.isdigit():
                if j + len(seg) > len(word) or word[j : j+len(seg)] != seg:
                    return False
                else:
                    j += len(seg)
            else:
                num = int(seg)
                if j + num > len(word):
                    return False
                else:
                    j += num
        # We can just return True here, but adding this can check the case where len(abbr) = 0
        return j == len(word)
