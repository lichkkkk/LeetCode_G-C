/**
 * 93. Restore IP Addresses
 * Tag: Backtracking
 * Running Time: Require to traverse all possible combinations -> O(n^3)
 * Chang Li at UC San Diego
 * Jan. 9, 2016
 */

class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string>* res = new vector<string>;
        helper(*res, s, "", 4);
        return *res;
    }
    
     void helper(vector<string>& res, string s, string tmp, int n) {
        if(n == 0 && s.size() == 0) res.push_back(tmp.substr(1, tmp.size()-1));
        else if(n != 0) {
            int pos = 1;
            while(pos < 4 && pos <= s.size()) {
                string seg = s.substr(0, pos);
                if(seg.size() == 1 || (seg[0] != '0' && atoi(seg.c_str()) < 256)) {
                    helper(res, s.substr(pos, s.size()-pos), tmp+"."+seg, n-1);
                }
                pos ++;
            }
        }
    }
};
