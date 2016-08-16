/**
 * 128. Longest Consecutive Sequence
 *
 * Chang Li @ Sunnyvale
 */
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> set(nums.begin(), nums.end());
        int max_len = 0;
        for (int n : nums) {
            if (set.find(n-1) == set.end()) {
                int len = 1;
                n++;
                while (set.find(n) != set.end()) {
                    len++;
                    n++;
                }
                max_len = max(max_len, len);
            }
        }
        return max_len;
    }
};
