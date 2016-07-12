/**
 * 332. Reconstruct Itinerary
 * 
 * Chang Li @ Mountain View
 * Jul. 10, 2016
 */
class Solution {
public:
    vector<string> findItinerary(vector<pair<string, string>> tickets) {
        for (const auto& p : tickets) {
            table[p.first].insert(p.second);
        }
        visit("JFK");
        return vector<string>(res.rbegin(), res.rend());
    }
    
    unordered_map<string, multiset<string>> table;
    vector<string> res;
    
    void visit(string next_stop) {
        while (table[next_stop].size()) {
            string new_next_stop = *table[next_stop].begin();
            table[next_stop].erase(table[next_stop].begin());
            visit(new_next_stop);
        }
        res.push_back(next_stop);
    }
};
