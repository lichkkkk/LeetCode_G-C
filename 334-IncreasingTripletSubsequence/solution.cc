/**
 * 334. Increasing Triplet Subsequence
 * 
 * Chang Li @ Mountain View
 * Jul. 13, 2016
 */
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        if (nums.empty()) return false;
        
        vector<bool> has_bigger(nums.size(), false);
        int max = nums.back();
        for (int i=nums.size()-2; i>=0; --i) {
            if (nums[i] < max) {
                has_bigger[i] = true;
            } else {
                max = nums[i];
            }
        }
        vector<bool> has_smaller(nums.size(), false);
        int min = nums.front();
        for (int i=1; i<nums.size(); ++i) {
            if (nums[i] > min) {
                has_smaller[i] = true;
            } else {
                min = nums[i];
            }
        }
        for (int i=1; i<nums.size()-1; ++i) {
            if (has_bigger[i] && has_smaller[i]) {
                return true;
            }
        }
        return false;
    }
};
