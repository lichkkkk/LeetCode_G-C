/**
 * 365. Water and Jug Problem
 * 
 * Chang Li @ Mountain View
 * Jul. 4, 2016
 */
class Solution {
public:
    bool canMeasureWater(int x, int y, int z) {
        vector<int> table(x+y+1, 0);
        table[x] = 1;    // 1 = ok; 0 = unset; -1 = not ok
        table[y] = 1;
        table[0] = 1;

        return CanMeasureWaterImpl(table, x, y, z);
    }
    
    bool CanMeasureWaterImpl(vector<int>& table, int x, int y, int z) {
        if (z < 0 || z > x+y) return false;
        
        if (table[z] == 0) {
            table[z] = -1;
            if (CanMeasureWaterImpl(table, x, y, z-x)
                    || CanMeasureWaterImpl(table, x, y, z-y)
                    || CanMeasureWaterImpl(table, x, y, x-(y-z))
                    || CanMeasureWaterImpl(table, x, y, y-(x-z))) {
                table[z] = 1;
            }
        }
        
        return table[z] == 1;
    }
};
