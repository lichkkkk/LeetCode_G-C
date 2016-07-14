/**
 * 300. Longest Increasing Subsequence
 * 
 * Chang Li @ Mountain view
 * Jul. 13, 2016
 */
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> table;
        map<int, int> path_map;
        for (int n : nums) {
            auto it = lower_bound(table.begin(), table.end(), n);
            
            if (it == table.begin()) path_map[n] = n;
            else path_map[n] = *(it-1);
            
            if (it == table.end()) table.push_back(n);
            else *it = n;
        }
        
        // Reconstruct the LIS path
        vector<int> path;
        int n = table.back();
        path.push_back(n);
        while (path_map[n] != n) {
            n = path_map[n];
            path.push_back(n);
        }
        for (auto it=path.rbegin(); it!=path.rend(); ++it) {
            cout << *it << " ";
        }
        
        return table.size();
    }
};
