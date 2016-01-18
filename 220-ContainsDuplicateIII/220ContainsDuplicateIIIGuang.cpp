class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        // time complexity:  n * logk 
        if(t<0 || k<=0 || nums.size() <=1) return false;
        set<int> si;
        si.insert(nums[0]);
        int start = 1;
        while(start < nums.size()){
            if(si.size() == k+1)
                si.erase(nums[start-k-1]);
            auto ret = si.insert(nums[start]);
            if(ret.second == false) return true;
            auto it = ret.first;
            if(it != si.begin()){
                auto it_ = it;
                it_ --;
                if((long long)*it - *(it_) <= t) return true;
            }
            auto it_ = it;
            it_ ++;
            //printf("back\n");
            if(it_ != si.end() && (long long)*(it_) - *it <= t) return true;
            start++;
        }
        return false;
    }
};