/**
 * 172. Factorial Trailing Zeroes
 * 
 * Chang Li @ Avalon Silicon Valley
 * Jul. 18, 2016
 */
class Solution {
public:
    int trailingZeroes(int n) {
        return n >= 5 ? n/5 +trailingZeroes(n/5) : 0;
    }
};
