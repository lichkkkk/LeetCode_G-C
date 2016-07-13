class Solution {
public:
    vector<string> res;
    unordered_map<string, map<string, int>> trips;
    vector<string> findItinerary(vector<pair<string, string>> tickets) {
        tickets.push_back(make_pair(string("start"), string("JFK")));
        for(auto &p : tickets)
            trips[p.first][p.second]++;
        stack<string> S;
        S.push("JFK");
        res.push_back("start");
        while(!S.empty()){
            auto cur = S.top();
            S.pop();
            trips[res.back()][cur]--;
            res.push_back(cur);
            // add all next trip
            bool hasNext = false;
            for(auto it = trips[cur].rbegin(); it != trips[cur].rend(); it++)
                if(it->second){
                    S.push(it->first);
                    hasNext = true;
                }
            if(!hasNext){
                if(res.size() == tickets.size()+1)
                    return vector<string>(res.begin()+1, res.end());
                // go back, may be more than one step
                while(trips[cur].find(S.top()) == trips[cur].end() || trips[cur][S.top()] == 0){
                    res.pop_back();
                    trips[res.back()][cur]++;
                    cur = res.back();
                }
            }
        }
        return res;//for compiler complain
    }
};
