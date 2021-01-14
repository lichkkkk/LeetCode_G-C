class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& A) {
        vector<vector<int>> AT;
        for (int i=0; i<A[0].size(); i++) {
            vector<int> row;
            for (int j=0; j<A.size(); j++) {
                row.push_back(A[j][i]);
            }
            AT.push_back(row);
        }
        return AT;
    }
};
// We can improve this by avoiding copy
