/**
 * 89. Gray Code
 * Chang Li
 * Jan. 2, 2016
 */

class Solution {
public:
    vector<int> grayCode(int n) {
        if(n == 0) return *(new vector<int>(1,0));
        
        vector<int> first_half = grayCode(n-1);
        vector<int> second_half;
        // Construct the 2nd half
        for(int i=first_half.size()-1; i>=0; i--) {
            second_half.push_back(first_half[i] + pow(2, n-1));
        }
        // Merge
        for(int i=0; i<second_half.size(); i++) {
            first_half.push_back(second_half[i]);
        }
        return first_half;
    }
};
