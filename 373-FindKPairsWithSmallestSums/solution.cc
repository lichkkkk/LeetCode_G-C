/**
 * 373. Find K Pairs with Smallest Sums
 * 
 * Chang Li @ Mountain View
 * Jul. 6, 2016
 */
class Solution {
public:
    using sum_pair = pair<int, pair<int, int>>;
    vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<pair<int, int>> res;
        if (k <= 0 || nums1.empty() || nums2.empty()) return res;
        
        auto comp = [](sum_pair& a, sum_pair& b) { return a.first > b.first; };
        priority_queue<sum_pair, vector<sum_pair>, decltype(comp)> queue(comp);

        for (auto it=nums2.begin(); it!=nums2.end(); ++it) {
            queue.push(sum_pair(nums1.front()+*it, pair<int, int>(0, it-nums2.begin())));
        }
        
        for (int i=0; i<k; ++i) {
            if (queue.empty()) break;
            int index_1 = queue.top().second.first;
            int index_2 = queue.top().second.second;
            queue.pop();
            res.push_back(pair<int, int>(nums1[index_1], nums2[index_2]));
            if (++index_1 < nums1.size()) {
                queue.push(sum_pair(nums1[index_1]+nums2[index_2], pair<int, int>(index_1, index_2)));
            }
        }
        
        return res;
    }
};
