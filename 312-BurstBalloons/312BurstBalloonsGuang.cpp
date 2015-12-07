const int N = 512;    
int c[N][N] = {0};
int v[N][N] = {0};
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        return run(nums, 0, nums.size()-1, 1, 1);
    }
    int run(vector<int>& nums, int i, int j, int l, int r){
        if(i > j) return 0;
        if(v[i][j]) return c[i][j];
        int coin = 0;
        for(int k = i; k <= j; k++){
            coin = max(coin, run(nums, i, k-1, l, nums[k]) \
                           + l*nums[k]*r \
                           + run(nums, k+1, j, nums[k], r));
        }
        v[i][j] = 1;
        c[i][j] = coin;
        return coin;
    }
};
