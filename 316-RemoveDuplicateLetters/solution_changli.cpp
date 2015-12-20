/**
 * Greedy + stack
 *
 * Chang Li at UC San Diego
 * Dec. 19, 2015
 */

class Solution {
public:
    string removeDuplicateLetters(string s) {
        int count[26] = {0};
        for(int i=0; i<s.size(); i++) {
            count[s[i]-'a'] ++;
        }
        int pos = 0;
        string res = "";
        bool already_in[26] = {false};
        
        while(pos < s.size()) {
            
            count[s[pos] - 'a'] --;
            if(!already_in[s[pos]-'a']) {
            
                while(res.size() > 0 && res.back() > s[pos] && count[res.back()-'a'] > 0) {
                    already_in[res.back() - 'a'] = false;
                    res.pop_back();
                }
                res.push_back(s[pos]);
                already_in[s[pos] - 'a'] = true;
            }
            
            pos++;
        }
        return res;
    }
};
