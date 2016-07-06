/**
 * 356. Line Reflection
 * 
 * Chang Li @ Mountain View
 * Jul. 5, 2016
 */
class Solution {
public:
    bool isReflected(vector<pair<int, int>>& points) {
        if (points.empty()) return true;
        
        sort(points.begin(), points.end());
        
        sort(points.begin()+(points.size()/2), points.end(), 
                [](pair<int, int>& a, pair<int, int>& b){ 
                    if (a.first != b.first) return a.first < b.first;
                    else return b.second < a.second;
                });
        
        auto begin = points.begin();
        auto end = points.end()-1;
        float pivot = (begin->first + end->first) / 2.0;
        while (begin <= end) {
            // Check y axis
            if (begin->first != end->first && begin->second != end->second) {
                return false;
            }
            // Check x axis
            float new_pivot = (begin->first + end->first) / 2.0;
            if (new_pivot != pivot) {
                return false;
            }
            pivot = new_pivot;
            // Move two pointers
            do {++begin;} while (*(begin-1) == *begin);
            do {--end;} while (*(end+1) == *end);
        }
        return true;
    }
};
