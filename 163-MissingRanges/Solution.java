/**
 * 163. Missing Ranges
 * Tag: Array
 *      Nothing special. Just take care of some corner cases.
 * Chang Li at UC San Diego
 * Feb. 22, 2016
 */

public class Solution {
    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        List<String> res = new LinkedList<>();
        
        // Deal with empty array
        if (nums == null || nums.length == 0) {
            if (upper >= lower) {
                res.add(getInterval(lower, upper));
            }
            return res;
        }
        
        // Deal with the beginning 
        if (nums[0] - lower > 0) {
            res.add(getInterval(lower, nums[0]-1));
        }
        
        // Deal with the body part
        int pos = 1;
        while (pos < nums.length) {
            if (nums[pos]-nums[pos-1] > 1 && nums[pos-1] >= lower && nums[pos] <= upper) {
                res.add(getInterval(nums[pos-1]+1, nums[pos]-1));
            }
            pos ++;
        }
        
        // Deal with the tailing
        if (upper-nums[nums.length-1] > 0) {
            res.add(getInterval(nums[nums.length-1]+1, upper));
        }
        
        return res;
    }
    
    public String getInterval(int start, int end) {
        String interval;
        if (end == start) {
            interval = start + ""; 
        } else {
            interval = start + "->" + end;
        }
        return interval;
    }
}
