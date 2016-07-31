/**
 * 57. Insert Interval
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
    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
        int start_pos = find_last_smaller(intervals, newInterval.start);
        int end_pos = find_first_bigger(intervals, newInterval.end);
        if (start_pos % 2 == 0) {
            newInterval.start = intervals[start_pos/2].start;
        }
        if (end_pos % 2 == 1) {
            newInterval.end = intervals[end_pos/2].end;
        }
        intervals.erase(intervals.begin()+(start_pos+1)/2,
                        intervals.begin()+(end_pos+1)/2);
        intervals.insert(intervals.begin()+(start_pos+1)/2, newInterval);
        return intervals;
    }
    
    int find_last_smaller(vector<Interval>& intervals, int target) {
        if (intervals.empty() || target <= intervals.front().start) return -1;
        int left = 0, right = intervals.size();
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (intervals[mid].start < target) {
                left = mid;
            } else {
                right = mid;
            }
        }
        return (intervals[left].end < target) ? left*2+1 : left*2;
    }
    
    int find_first_bigger(const vector<Interval>& intervals, int target) {
        if (intervals.empty() || target >= intervals.back().end)
          return intervals.size()*2;
        int left = -1, right = intervals.size()-1;
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (intervals[mid].end > target) {
                right = mid;
            } else {
                left = mid;
            }
        }
        return (intervals[right].start > target) ? right*2 : right*2+1;
    }
};
