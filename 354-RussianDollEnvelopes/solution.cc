/**
 * 354. Russian Doll Envelopes
 * 
 * Chang Li @ Mountain view
 * Jul. 13, 2016
 */
class Solution {
public:

    int maxEnvelopes(vector<pair<int, int>>& envelopes) {
        // Sort (Cumtomerized Comp func is necessary)
        sort(envelopes.begin(), envelopes.end(),
                [](const pair<int, int>& a, const pair<int, int>& b) {
                    if (a.first == b.first) return a.second > b.second;
                    else return a.first < b.first;
                });
        // Find Longest Increasing Sequence
        vector<int> table;
        for (auto p : envelopes) {
            auto it = lower_bound(table.begin(), table.end(), p.second);
            if (it == table.end()) table.push_back(p.second);
            else *it = p.second;
        }
        return table.size();
    }
};
