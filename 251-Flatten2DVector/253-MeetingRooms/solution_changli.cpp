/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 *
 * Chang Li
 * Dec. 31, 2015
 */
class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {
        if(intervals.size() == 0) return 0;
        int start_time[intervals.size()];
        int end_time[intervals.size()];
        for(int i=0; i<intervals.size(); i++) {
            start_time[i] = intervals[i].start;
            end_time[i] = intervals[i].end;
        }
        sort(start_time, start_time + intervals.size());
        sort(end_time, end_time + intervals.size());
        int start_pos = 0;
        int end_pos = 0;
        int rooms = 0;
        int min_rooms = 0;
        while(start_pos < intervals.size() && end_pos < intervals.size()) {
            if(start_time[start_pos] < end_time[end_pos]) {
                rooms ++;
                min_rooms = max(min_rooms, rooms);
                start_pos ++;
            }else {
                rooms --;
                end_pos ++;
            }
        }
        return min_rooms;
    }
};
