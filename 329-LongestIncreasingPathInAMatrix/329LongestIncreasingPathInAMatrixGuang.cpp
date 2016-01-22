class Solution {
// tiny yao'kai'xin要开心    ha哈   ai'ni爱你 
public:
int row, col;
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        row = matrix.size();
        if(row == 0) return 0;
        int ret = 0;
        col = matrix[0].size();
        vector<vector<int>> path(row, vector<int>(col, 0));
        for(int i = 0; i < row; i++)
            for(int j = 0; j < col; j++)
                if(path[i][j] != 1)ret = max(dfs(matrix, path, i, j), ret);
        return ret;
    }
    int dfs(vector<vector<int>>& m, vector<vector<int>>& p, int i, int j){
        if(p[i][j]) return p[i][j];
        for(int l = i-1; l <= i+1; l++)
            for(int k = j-1; k <= j+1; k++){
                if(l>=0 && l<=row-1 && k>=0 && k<=col-1 && (l+k - i - j >= -1) && (l+k - i - j <= 1) && (l+k - i - j != 0) && m[i][j] > m[l][k])
                    p[i][j] = max(p[i][j], dfs(m, p, l, k)+1);
            }    
        return p[i][j]? p[i][j] : 1;
    }
};
