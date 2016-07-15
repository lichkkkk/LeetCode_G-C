/**
 * 286. Walls and Gates
 * 
 * Chang Li @ Mountain view
 * Jul. 13, 2016
 */
class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        for (int i=0; i<rooms.size(); ++i) {
            for (int j=0; j<rooms[0].size(); ++j) {
                if (rooms[i][j] == 0) {
                    minDistance(rooms, i, j, 0);
                }
            }
        }
    }
    
    void minDistance(vector<vector<int>>& rooms, int x, int y, int dis) {
        if (rooms[x][y] < dis) return;
        rooms[x][y] = dis;
        
        if (x > 0 && rooms[x-1][y] > -1) {
            minDistance(rooms, x-1, y, dis+1);
        }
        if (y < rooms[0].size()-1 && rooms[x][y+1] > -1) {
            minDistance(rooms, x, y+1, dis+1);
        }
        if (x < rooms.size()-1 && rooms[x+1][y] > -1) {
            minDistance(rooms, x+1, y, dis+1);
        }
        if (y > 0 && rooms[x][y-1] > -1) {
            minDistance(rooms, x, y-1, dis+1);
        }
    }
};
