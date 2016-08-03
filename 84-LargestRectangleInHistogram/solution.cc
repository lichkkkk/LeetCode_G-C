/**
 * 84. Largest Rectangle in Histogram
 * 
 * Chang Li @ Sunnyvale
 * Aug. 1, 2016
 */
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        maxArea_ = 0;
        for (int i=0; i<heights.size(); ++i) {
            PushAndUpdate(i, heights[i]);
        }
        PushAndUpdate(heights.size(), 0);
        return maxArea_;
    }
    
private:
    void PushAndUpdate(int ind, int height) {
        while (!stack_.empty() && stack_.back().second>height) {
            int width = ind-(stack_.size()>1 
                               ? stack_[stack_.size()-2].first-1
                               : 0);
            maxArea_ = max(maxArea_, width * stack_.back().second);
            stack_.pop_back();
        }
        stack_.emplace_back(ind, height);
    }
    
    int maxArea_ = 0;
    vector<pair<int, int>> stack_;
};
