class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr_split = []
        l, r = 0, 1
        while r <= len(abbr):
            while r < len(abbr) and (abbr[l].isdigit() == abbr[r].isdigit()):
                r += 1
            abbr_split.append(abbr[l:r])
            l = r
            r += 1
        abbr_expand = ''
        for i, s in enumerate(abbr_split):
            if s[0] == '0':
                return False
            if i > 0 and s[0].isdigit() and abbr_split[i-1][0].isdigit():
                return False
            if s[0].isdigit():
                if len(abbr_expand) + int(s) > len(word):  # forgot this line and got MLE
                    return False
                abbr_expand += '.' * int(s)
            else:
                abbr_expand += s
        if len(abbr_expand) != len(word):
            return False
        for i in range(len(word)):
            if word[i] != abbr_expand[i] and abbr_expand[i] != '.':
                return False
        return True
