class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> table;
        vector<int> stack;
        for (int n : nums2) {
            while (!stack.empty() && stack.back() < n) {
                table[stack.back()] = n;
                stack.pop_back();
            }
            stack.push_back(n);
        }
        for (int n : stack) table[n] = -1;
        vector<int> res;
        for (int n : nums1) res.push_back(table[n]);
        return res;
    }
};
