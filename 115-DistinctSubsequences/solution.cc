/**
 * 115. Distinct Subsequences
 * 
 * Chang Li @ MTV-47-1-Track
 * Aug. 3, 2016
 */
class Solution {
public:
    int numDistinct(string s, string t) {
        vector<int> table(t.size()+1, 0);
        table[t.size()] = 1;
        for (int si=s.size()-1; si>=0; --si) {
            for (int ti=0; ti<t.size(); ++ti) {
                table[ti] += s[si]==t[ti] ? table[ti+1] : 0;
            }
        }
        return table[0];
    }
