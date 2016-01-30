class Solution {
public:
    int hIndex(vector<int>& citations) {
        if(!citations.size()) return 0;
        int l = -1; int h = citations.back() + 1;
        auto start = citations.begin();
        auto end = citations.end();
        auto last = end;
        while(l < h-1){
            int m = l + (h-l)/2;
            auto pos = lower_bound(start, end, m);
            int cnt = last - pos;
            if(cnt >= m){
                l = m;
                start = pos; 
            }else{
                h = m;
                end = pos;
            }
        }
        return l;
    }
};
