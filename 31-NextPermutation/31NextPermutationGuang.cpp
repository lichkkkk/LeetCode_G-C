class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        // 1 2 3 -> 1 3 2 -> 2 1 3 -> 2 3 1 -> 3 1 2 -> 3 2 1
        
        //
        //
        int len = nums.size();
        for(int i = len - 1; i>=1; i--)
                if(nums[i] > nums[i-1]){
                    int k = i;
                    for(int j = i; j < len; j++){
                        if(nums[j] <= nums[i-1]) continue;
                        if(nums[j] < nums[k]) k = j;
                    }
                    int tmp = nums[i-1];
                    nums[i-1]= nums[k];
                    nums[k] = tmp;
                    sort(nums.begin()+i, nums.end());
                    return;
                }
        
        
        sort(nums.begin(), nums.end());
        
    }
};
