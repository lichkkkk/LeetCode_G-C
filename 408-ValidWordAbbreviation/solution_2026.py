class Solution:
    def validWordAbbreviation2(self, word: str, abbr: str) -> bool:
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

    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        pw, pa = 0, 0
        while pa < len(abbr):
            if pw >= len(word):
                return False
            if abbr[pa].isdigit():
                if abbr[pa] == '0':
                    return False
                pa_past = pa
                pa += 1
                while pa < len(abbr):
                    if abbr[pa].isdigit():
                        pa += 1
                    else:
                        break
                cnt = int(abbr[pa_past:pa])
                pw += cnt
            else:
                if abbr[pa] != word[pw]:
                    return False
                pa += 1
                pw += 1
        return pw == len(word)      
