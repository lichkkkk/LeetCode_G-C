/**
 * 325. Maximum Size Subarray Sum Equals k
 * 
 * Chang Li @ Mountain view
 * Jul. 11, 2016
 */
class Solution {
public:
    int maxSubArrayLen(vector<int>& nums, int k) {
        unordered_map<int, int> sum_map;
        int sum = 0;
        sum_map[sum] = -1;
        int max_len = 0;
        for (int i=0; i<nums.size(); ++i) {
            sum += nums[i];
            if (sum_map.find(sum) == sum_map.end()) {
                sum_map[sum] = i;
            }
            if (sum_map.find(sum-k) != sum_map.end()) {
                max_len = max(max_len, i-sum_map[sum-k]);
            }
        }
        return max_len;
    }
};
