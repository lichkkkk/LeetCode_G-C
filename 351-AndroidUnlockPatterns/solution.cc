/**
 * 351. Android Unlock Patterns
 * 
 * Chang Li @ Mountain View
 * Jul. 7, 2016
 */
class Solution {
public:
    int numberOfPatterns(int m, int n) {
        vector<vector<int>> screen(3, vector<int>(3, 0));
        return countPatterns(0, screen, 0, m, n)*4 + 
                countPatterns(1, screen, 0, m, n)*4 +
                countPatterns(4, screen, 0, m, n);
    }
    
    int countPatterns(int start_key, vector<vector<int>>& screen, int curr_len,
                        int min_len, int max_len) {
        curr_len += 1;
        if (curr_len > min(max_len, 9)) {
            return 0;
        } else if (curr_len == max_len) {
            return 1;
        }
        
        int x = start_key % 3;
        int y = start_key / 3;
        
        int pattern_count = 0;
        screen[x][y] = 1;
        for (int key : availableKeys(start_key, screen)) {
            pattern_count += countPatterns(key, screen, curr_len, min_len, max_len);
        }
        screen[x][y] = 0;
        return pattern_count + ((curr_len >= min_len) ? 1 : 0);
    }
    
    vector<int> availableKeys(int curr_key, const vector<vector<int>>& screen) {
        vector<int> available_keys;
        int curr_x = curr_key % 3;
        int curr_y = curr_key / 3;
        for (int key=0; key<9; ++key) {
            int x = key % 3;
            int y = key / 3;
            if (screen[x][y] == 1) {
                continue;
            } else if ((x+curr_x)%2 == 0 && (y+curr_y)%2 == 0) {
                if (screen[(x+curr_x)/2][(y+curr_y)/2] == 1) {
                    available_keys.push_back(key);
                }
            } else {
                available_keys.push_back(key);
            }
        }
        return available_keys;
    }
};
