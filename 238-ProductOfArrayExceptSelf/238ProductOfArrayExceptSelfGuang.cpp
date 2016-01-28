class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        // vector<int> ret(nums.size(), 0);
        // vector<int> indexOfZero;
        // for(int i = 0; i< nums.size();i++)
        //     if(nums[i] == 0)
        //         indexOfZero.push_back(i);
        // if(indexOfZero.size()>=2) return ret;
        // if(indexOfZero.size() == 1){
        //     int j = indexOfZero[0];
        //     ret[j] = 1;
        //     for(int i = 0;i < nums.size(); i++){
        //         if(i == j) continue;
        //         ret[j] *= nums[i];
        //     }
        //     return ret;
        // }
        // ret[0] = 1;
        // for(int i = 1; i < nums.size(); i++)
        //     ret[0] *= nums[i];
        // for(int i = 1; i < nums.size(); i++)
        //     ret[i] = ret[i-1]*nums[i-1]/nums[i];
        // return ret;
        
        
        vector<int> ret(nums.size(), 1);
        int left, right;
        left = right = 1;
        for(int i = 0; i < nums.size(); i++){
            ret[i] = left;
            left *= nums[i];    
        }
        for(int i = nums.size()-1; i >=0; i--){
            ret[i] *= right;
            right *= nums[i];    
        }        
        return ret;
        
    }
};
