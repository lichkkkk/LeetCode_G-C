class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        vector<int> ret;
        sort(nums.begin(), nums.end());
        int i = 0;
        while(i < nums.size()-1){
            if(nums[i] == nums[i+1]) i+=2;
            else{
                ret.push_back(nums[i]);
                i++;
            }
        }
        if(i == nums.size()-1) ret.push_back(nums[i]);
        return ret;
    }
};
