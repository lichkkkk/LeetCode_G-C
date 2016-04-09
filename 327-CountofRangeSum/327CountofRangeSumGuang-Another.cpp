#define ll long long 
class Solution {
public:
    vector<ll> sum;
    int h, l;
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        sum.push_back(0);
        for(auto n : nums)
            sum.push_back(sum.back()+n);
        h = upper;
        l = lower;
        
        return merge_cnt(sum.begin(), sum.end());    
    }

    int merge_cnt(vector<ll>::iterator beg, vector<ll>::iterator end){
        int res = 0;
        if(end - beg <= 1)
            return res;
        auto mid = beg + (end-beg)/2;
        res += merge_cnt(beg, mid);
        res += merge_cnt(mid, end);
        for(auto it = mid; it != end; ++it){
            // a[j] = *it
            // l <= a[j] - a[i] <= h  => a[j]-h <= a[i] <= a[j]-l
            auto p = lower_bound(beg, mid, (*it)-h);
            if(p == mid) continue;
            auto q = upper_bound(beg, mid, (*it)-l);
            if(q == beg) continue;
            q--;
            res += q-p+1;
        }
        merge(beg, mid, mid, end);
        return res;
    }
    void merge(vector<ll>::iterator b1, vector<ll>::iterator e1, vector<ll>::iterator b2, vector<ll>::iterator e2){
        vector<ll> res;
        auto pos = b1;
        while(b1 != e1 && b2 != e2){
            if(*b1 <= *b2){
                res.push_back(*b1);
                ++b1;
            }else{
                res.push_back(*b2);
                ++b2;
            }
        }
        while(b1 != e1){
            res.push_back(*b1);
            ++b1;
        }
        while(b2 != e2){
            res.push_back(*b2);
            ++b2;
        }
        for(auto n : res)
            *(pos++) = n;
    }
};
