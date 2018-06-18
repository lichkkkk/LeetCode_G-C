class Solution {
public:
    vector<string> res;
    map<string, map<string, int>> trips;
    int cnt = 0;
    vector<string> findItinerary(vector<pair<string, string>> tickets) {
        for(auto &p : tickets)
            trips[p.first][p.second]++;
        cnt = tickets.size() + 1;
        dfs("JFK");
        return res;
    }
    bool dfs(string cur){
        res.push_back(cur);
        if(res.size() == cnt)
            return true;
        for(auto it = trips[cur].begin(); it != trips[cur].end(); it++){
            if(trips[cur][it->first]){
                --trips[cur][it->first];
                if(dfs(it->first))
                    return true;
                ++trips[cur][it->first];
            }
        }
        res.pop_back();
        return false;
    }
};
