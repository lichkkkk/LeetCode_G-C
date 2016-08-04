/**
 * 85. Maximal Rectangle
 * 
 * Chang Li @ MTV-47-1-Track
 * Aug. 3, 2016
 */
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.empty()) return 0;
        vector<vector<int>> table = MakeTable(matrix);
        int maxRec = 0;
        for (const auto& heights : table) {
            maxRec = max(maxRec, largestRectangleArea(heights));
        }
        return maxRec;
    }
    
private:
    vector<vector<int>> MakeTable(const vector<vector<char>>& matrix) {
        vector<vector<int>> table;
        vector<int> row(matrix[0].size(), 0);
        for (const vector<char>& vec : matrix) {
            for (int i=0; i<vec.size(); ++i) {
                row[i] = vec[i]=='1' ? row[i]+1 : 0;
            }
            table.push_back(row);
        }
        return table;
    }

    int largestRectangleArea(const vector<int>& heights) {
        maxArea_ = 0;
        stack_.clear();
        for (int i=0; i<heights.size(); ++i) {
            PushAndUpdate(i, heights[i]);
        }
        PushAndUpdate(heights.size(), 0);
        return maxArea_;
    }
    
    void PushAndUpdate(int ind, int height) {
        while (!stack_.empty() && stack_.back().second>height) {
            int width = ind - (stack_.size()>1
                                  ? stack_[stack_.size()-2]-1.first
                                  : 0);
            maxArea_ = max(maxArea_, width * stack_.back().second);
            stack_.pop_back();
        }
        stack_.emplace_back(ind, height);
    }
    
    int maxArea_ = 0;
    vector<pair<int, int>> stack_;
};
