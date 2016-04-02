/**
 * 338. Counting Bits
 * 
 *      If n is even, then f(n+1) = f(n) + 1; if n is odd, then f(n+1) = f(n/2 + 1).
 * 
 * Chang Li at UC San Diego
 * Apr. 2, 2016
 */

class Solution {
public:
    vector<int> countBits(int num) {
        
        vector<int> res = *(new vector<int>(num + 1, 0));
        if (num == 0) return res;
        
        res[1] = 1;   // f(1) = 1
        
        for (int i = 1; i < num; i++) {
            if (i % 2 == 0) {
                res[i+1] = res[i] + 1;
            } else {
                res[i+1] = res[i/2 + 1];
            }
        }
        
        return res;
    }
};
