//  transverse  and then mirror

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        for(int i = 0; i<matrix.size();++i)
            for(int j = i+1; j < matrix[0].size();++j)
                swap(matrix, i, j, j, i);
        for(int i = 0; i<matrix.size();++i)
            for(int j = 1; j <= matrix[0].size()/2; ++j)
                swap(matrix, i, j-1, i, matrix[0].size() - j);
    }
    
    
    inline void swap(vector<vector<int>>& matrix, int i_1, int j_1, int i_2, int j_2){
        auto tmp = matrix[i_1][j_1];
        matrix[i_1][j_1] = matrix[i_2][j_2];
        matrix[i_2][j_2] = tmp;
    }
};
