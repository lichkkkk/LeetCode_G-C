/**
 * 344. Reverse String
 * 
 * Chang Li @ Mountain View
 * Jul. 5, 2016
 */
class Solution {
public:
    string reverseString(string s) {
        string res = "";
        for (auto it=s.end()-1; it>=s.begin(); it--) {
            res.push_back(*it);
        }
        return res;
    }
};
