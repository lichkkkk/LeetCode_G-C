class Solution {
public:
    void sortColors(vector<int>& nums) {
        //.....
        //sort(nums.begin(), nums.end());
        
        // not one pass
        // int zero, one, two;
        // zero = one = two = 0;
        // for(auto num : nums)
        //     if(num == 0) ++zero;
        //     else if(num == 1) ++one;
        //     else ++two;
        // auto it = nums.begin();
        // fill(it, it+zero, 0);
        // fill(it+zero, it+zero+one, 1);
        // fill(it+zero+one, nums.end(), 2);
        
        
        int zero = 0, two = nums.size() - 1;
        int i = zero;
        while(i < two+1){
            if(nums[i] == 2) {
                swap(nums[i], nums[two]);
                two --;
                continue;
            }else if(nums[i] == 0){
                swap(nums[i], nums[zero]);
                zero ++;
                i++;
                continue;
            }
            i++;
        }
    }
    
};
