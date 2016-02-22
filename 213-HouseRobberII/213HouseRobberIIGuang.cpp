class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.empty()) return 0;
        if(nums.size() == 1) return nums[0];
        if(nums.size() == 2) return max(nums[0], nums[1]);
        return max(   rob_help(vector<int>(nums.begin()+1, nums.end())), 
                      rob_help(vector<int>(nums.begin()+2, nums.end()-1)) + nums[0]);
    }
    int rob_help(vector<int> nums) {
        int withSelf, withoutSelf;
        withSelf = withoutSelf = 0;
        int ret = 0;
        for(int i = 0; i < nums.size(); ++i){
            auto tmp = withSelf;
            withSelf = withoutSelf + nums[i];
            withoutSelf = max(tmp, ret);
            ret = max(withSelf, withoutSelf);
        }
        return ret;    
    }
};
