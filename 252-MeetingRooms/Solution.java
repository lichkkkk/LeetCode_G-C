/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 *
 * Sort and then check. Use a comparator here.
 *
 * Chang Li at UC San Diego
 * Dec. 14, 2015
 */
public class Solution {
    
    class Comp implements Comparator<Interval>{
        
        public int compare(Interval a, Interval b) {
            return a.start - b.start;
        }
        
        public boolean equals(Interval a, Interval b) {
            return a.start == b.start;
        }
        
    }
    
    public boolean canAttendMeetings(Interval[] intervals) {
        
        Arrays.sort(intervals, new Comp());
        for(int i=0; i<intervals.length-1; i++) {
            if(intervals[i].end > intervals[i+1].start) {
                return false;
            }
        }
        return true;
    }
}
