/**
 * 370. Range Addition
 * 
 * Chang Li @ Mountain View
 * Jun. 28, 2016
 */
class Solution {
public:
    vector<int> getModifiedArray(int length, vector<vector<int>>& updates) {
        
        vector<int> inc_table(length+1, 0);
        for (int i=0; i<updates.size(); ++i) {
            inc_table[updates[i][0]] += updates[i][2];
            inc_table[updates[i][1]+1] -= updates[i][2];
        }
        
        vector<int> res;
        int inc = 0;
        for (int i=0; i<length; ++i) {
            inc += inc_table[i];
            res.push_back(inc);
        }
        return res;
    }
};
