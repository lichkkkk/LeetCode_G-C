/**
 * 350. Intersection of Two Arrays II
 * 
 * Chang Li @ Mountain View
 * Jul. 5, 2016
 */
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, int> count_map;
        for (int num : nums1) {
            auto it = count_map.find(num);
            if (it == count_map.end()) {
                count_map.insert({num, 1});
            } else {
                it->second += 1;
            }
        }
        
        vector<int> res;
        for (int num : nums2) {
            auto it = count_map.find(num);
            if (it == count_map.end() || it->second == 0) {
                continue;
            } else {
                res.push_back(num);
                it->second -= 1;
            }
        }
        return res;
    }
};
