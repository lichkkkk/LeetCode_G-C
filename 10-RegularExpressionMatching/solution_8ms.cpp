/**
 * 10. Regular Expression Matching
 * Tag: Backtracking & DP
 * Chang Li, Apr. 11, 2016
 */
 
class Solution {
public:
    bool isMatch(string s, string p) {
        bool t[(s.length()+1)*p.length()];
        for (int i=0; i<(s.length()+1)*p.length(); i++)
            t[i] = true;
        return matchHelper(s, p, 0, 0, (bool*)t);
    }
    
private:
    bool matchHelper(string& s, string& p, int spos, int ppos, bool* table) {
        if (spos == s.length() && ppos == p.length()) {
            return true;
        } else if (ppos == p.length() || !table[spos*p.length()+ppos]) {
            return false;
        }
        bool withStar = false;
        char pchar = getNextElement(p, &withStar, ppos);
        if (!withStar) {
            if (spos < s.length() && (pchar == '.' || s[spos] == pchar)) {
                return matchHelper(s, p, spos+1, ppos+1, table);
            } else {
                table[spos*p.length()+ppos] = false;
                return false;
            }
        } else {
            for (int i=spos; i<s.length()+1; i++) {
                if (matchHelper(s, p, i, ppos+2, table)) {
                    return true;
                } else if (spos < s.length() && (pchar == '.' || s[i] == pchar)) {
                    continue;
                } else {
                    table[spos*p.length()+ppos] = false;
                    return false;
                }
            }
        }
    }

    char getNextElement(string& p, bool* star, int ppos) {
        if (ppos+1 < p.length()) {
            *star = (p[ppos+1] == '*');
        }
        return p[ppos];
    }
};
