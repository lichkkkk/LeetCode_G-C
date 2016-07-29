/**
 * 32. Longest Valid Parentheses
 *  Keep Calm And Carry On
 * Chang Li @ Sunnyvale
 * Jul. 28, 2016
 */
class Solution {
public:
    int longestValidParentheses(string s) {
        vector<int> len_table(s.size(), 0);
        int longest_len = 0;
        for (int i=s.size()-2; i>=0; --i) {
            if (s[i] == ')') continue;
            if (s[i+1] == ')') {
                len_table[i] = 2 + (i+2 < s.size() ? len_table[i+2] : 0);
            } else {
                int end_of_next = i+len_table[i+1];
                if (end_of_next+1 < s.size() && s[end_of_next+1] == ')') {
                    len_table[i] = 2 + len_table[i+1] + 
                        (end_of_next+2 < s.size() 
                            ? len_table[end_of_next+2] 
                            : 0);
                }
            }
            longest_len = max(longest_len, len_table[i]);
        }
        return longest_len;
    }
};
