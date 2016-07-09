/**
 * 343. Integer Break
 * 
 * Chang Li @ Mountain View
 * Jul. 9, 2016
 */
class Solution {
public:
    int integerBreak(int n) {
        vector<int> table(n+1, 0);
        table[1] = 1;
        
        int res = 0;
        for (int i=1; i<n; ++i) {
            res = max(res, i*integerBreakImpl(table, n-i));
        }
        return res;
    }
    
    int integerBreakImpl(vector<int>& table, int n) {
        if (table[n] == 0) {
            int max_product = 0;
            for (int i=1; i<n; ++i) {
                max_product = max(max_product, i*integerBreakImpl(table, n-i));
            }
            table[n] = max_product;
        };
        return max(n, table[n]);
    }
};
