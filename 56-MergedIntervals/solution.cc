/**
 * 56. Merge Intervals
 * 
 * Chang Li @ Sunnyvale
 * Jul. 30, 2016
 * 
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(), 
             [](const Interval& a, const Interval& b) {
                 return a.start < b.start;
             });
        vector<Interval> merged_vec;
        Interval* last = nullptr;
        for (const auto& i : intervals) {
            if (last == nullptr || last->end < i.start) {
                merged_vec.push_back(i);
                last = &merged_vec.back();
            } else {
                last->end = max(last->end, i.end);
            }
        }
        return merged_vec;
    }
};
