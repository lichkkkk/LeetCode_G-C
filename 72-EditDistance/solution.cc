/**
 * 72. Edit Distance
 * 
 * CHang Li @ GBUS
 * Aug. 1, 2016
 */
class Solution {
public:
    int minDistance(string word1, string word2) {
        vector<vector<int>> table(word1.size()+1, 
                                  vector<int>(word2.size()+1, -1));
        return minDistanceImpl(word1, word2, 0, 0, table);
    }
    
    int minDistanceImpl(const string& w1, const string& w2, int pos1, int pos2,
                        vector<vector<int>>& table) {
        if (pos1 == w1.size() && pos2 == w2.size()) {
            return 0;
        } else if (pos1 == w1.size()) {
            return w2.size() - pos2;
        } else if (pos2 == w2.size()) {
            return w1.size() - pos1;
        }
        if (table[pos1][pos2] < 0) {
            table[pos1][pos2] = min(
                minDistanceImpl(w1, w2, pos1, pos2+1, table) + 1,
                min(minDistanceImpl(w1, w2, pos1+1, pos2, table) + 1,
                    minDistanceImpl(w1, w2, pos1+1, pos2+1, table)+
                        (w1[pos1]==w2[pos2] ? 0 : 1)));
        }
        return table[pos1][pos2];
    }
};
