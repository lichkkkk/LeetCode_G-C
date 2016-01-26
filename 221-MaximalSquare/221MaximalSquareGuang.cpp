class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int row = matrix.size();
        if(row == 0) return 0;
        int col = matrix[0].size();
        vector<vector<int> > dp(row, vector<int>(col, 0));
        dp[0][0] = matrix[0][0]-'0';
        int l = dp[0][0];
        for(int k = 1; k < col + row - 1 ; k++){
            for(int i = 0; i < row; i++){
                int j = k - i;
                if(j < 0 || j >= col) continue;
                // dp[i][j] = 1/0? +  min{dp[i-1][j-1] dp[i-1][j] dp]i][j-1]}
                int m1 = i-1 < 0? 0 : dp[i-1][j];
                int m2 = j-1 < 0? 0 : dp[i][j-1];
                int m3 = (i-1 < 0 || j-1 < 0)? 0 : dp[i-1][j-1];
                int c = matrix[i][j] - '0';
                dp[i][j] = c == 0? 0 : c +  min(m3, min(m1, m2));
                l = max(dp[i][j], l);
                // printf("%d, %d : %d \n",i, j, l);
            }
        }
        return l*l;
    }
};
