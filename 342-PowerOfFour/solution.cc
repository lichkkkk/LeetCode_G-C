/**
 * 342. Power of Four
 * 
 * Chang Li @ Mountain view
 * Jul. 11, 2016
 */
class Solution {
public:
    bool isPowerOfFour(int num) {
        if (num == 1) return true;
        else if (num <= 0 || num & 3) return false;
        else return isPowerOfFour(num >> 2);
    }
};
