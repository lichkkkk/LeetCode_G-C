#define LL unsigned long long
class Solution {
public:
    LL prime = 17;
 
    LL hash(string s){
        LL p = 1;
        LL res = 0;
        for(auto c : s){
            res += (c-'a')*p;
            p *= prime;
        }
        return res;
    }
    LL rhash(string s){
        LL p = 1;
        LL res = 0;
        for(auto it = s.rbegin(); it != s.rend(); ++it){
            res += ((*it)-'a') * p;
            p *= prime;
        }
        return res;
    }
    unordered_map<string, pair<LL, LL>> hmap;
    vector<vector<int>> palindromePairs(vector<string>& words) {
        int n = words.size();        
        vector<vector<int>> res;
        // vector<LL> h, rh;
        // for(auto word : words){
        //     h.push_back(hash(word));
        //     rh.push_back(rhash(word));
        // }
        
        LL *h = new LL[n+4];
        LL *rh = new LL[n+4];
        int i = 0;
        for(auto word : words){
            h[i] = hash(word);
            rh[i] = rhash(word);
            ++i;
        }
        
        //vector<LL> p;
        LL p[100];
        LL t = 1;
        for(int i = 0; i < 100; i++){
            //p.push_back(t);
            p[i] = t;
            t *= prime;
        }
        for(int i = 0; i < n; i++){
            LL hi, hri, hj, hrj;
            hi = h[i], hri = rh[i];
            for(int j = i+1; j < n; j++){
                hj = h[j], hrj = rh[j];
                LL ij = hj*(LL)p[words[i].size()] + hi;
                LL ji = hi*(LL)p[words[j].size()] + hj;
                LL rjri = hri*(LL)p[words[j].size()] + hrj;
                LL rirj = hrj*(LL)p[words[i].size()] + hri;
                if(ij == rjri)// && isPal(words[i]+words[j]))
                    res.push_back(vector<int>({i, j}));
                if(ji == rirj)// && isPal(words[i]+words[j]))
                    res.push_back(vector<int>({j, i}));
            }
        }    
        return res;    
    }
};
