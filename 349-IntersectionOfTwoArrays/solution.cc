/**
 * 349. Intersection of Two Arrays
 * 
 * Chang Li @ Mountain View
 * Jul. 5, 2016
 */
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> nums1_set (nums1.begin(), nums1.end());
        set<int> res;
        for (int num : nums2) {
            auto it = nums1_set.find(num);
            if (it != nums1_set.end()) {
                res.insert(res.begin(), *it);
            }
        }
        return vector<int>(res.begin(), res.end());
    }
};
