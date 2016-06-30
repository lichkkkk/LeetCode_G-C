/**
 * 371. Sum of Two Integers
 * 
 * Chang Li @ Mountain View
 * Jun. 29, 2016
 */
class Solution {
public:
    int getSum(int a, int b) {
        
        int res = 0;
        int mask = 1;
        int carry = 0;
        
        while (mask != 0) {
            int a1 = a & mask;
            int b1 = b & mask;
            
            int count = 1;
            if (a1) count <<= 1;
            if (b1) count <<= 1;
            if (carry) count <<= 1;
            
            if (count == 1) {
                carry = 0;
            } else if (count == 2) {
                res |= mask;
                carry = 0;
            } else if (count == 4) {
                carry = 1;
            } else {
                res |= mask;
                carry = 1;
            }
            
            mask <<= 1;
        }
        return res;
    }
};
