// class Solution {
// public:
// int dp[100000] = {0};
// int numSquares(int n) {
//     if(n==0 || dp[n]) return dp[n];
//     if((int)sqrt(n) * (int)sqrt(n) == n) return 1;
    
//     int ret = 5;
//     for(int i = (int)sqrt(n) + 1; i > 0 && i >= (int) sqrt(n/4); i--){
//         if(n-i*i < 0 ) continue;
//         int m = numSquares(n - i*i);
//         ret = m+1<ret? m+1 : ret;
//         if(ret == 2) break;
//     }
//     return dp[n]=ret;
// }
// };
//http://www.cnblogs.com/grandyang/p/4800552.html
class Solution {
public:
    int numSquares(int n) {
        while (n % 4 == 0) n /= 4;
        if (n % 8 == 7) return 4;
        for (int a = 0; a * a <= n; ++a) {
            int b = sqrt(n - a * a);
            if (a * a + b * b == n) {
                return !!a + !!b;
            }
        }
        return 3;
    }
};
