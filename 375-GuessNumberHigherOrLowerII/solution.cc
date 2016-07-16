/**
 * 375. Guess Number Higher or Lower II
 * 
 * Chang Li @ Mountain view
 * Jul. 15, 2016
 */
class Solution {
public:
    int getMoneyAmount(int n) {
        vector<vector<int>> table(n+1, vector<int>(n+1, -1));
        return costInWorstCase(1, n, table);
    }
    
    int costInWorstCase(int from, int to, vector<vector<int>>& costTable) {
        if (from >= to) return 0;
        if (costTable[from][to] == -1) {
            int minMaxCost = 0x7FFFFFFF;
            for (int i=from; i<=to; ++i) {
                minMaxCost = min(minMaxCost, 
                                 i+max(costInWorstCase(from, i-1, costTable),
                                       costInWorstCase(i+1, to, costTable)));
            }
            costTable[from][to] = minMaxCost;
        }
        return costTable[from][to];
    }
};
