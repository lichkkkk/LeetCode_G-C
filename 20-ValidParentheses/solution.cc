class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        for (char ch : s) {
            if (ch == '(' || ch == '[' || ch == '{') {
                stack.push_back(ch);
            } else if (stack.empty()) {
                return false;
            } else if ((ch == ')' && stack.back() == '(')
                    || (ch == ']' && stack.back() == '[') 
                    || (ch == '}' && stack.back() == '{')) {
                stack.pop_back();
            } else {
                return false;
            }
        }
        return stack.empty();
    }
};
