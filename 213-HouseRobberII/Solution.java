/**
 * 213. House Robber II
 * Tag: DP
 *      A simple follow up of House Robber. Classic DP problem.
 * Chang Li at UC San Diego
 * Feb. 21, 2016
 */

public class Solution {
    public int rob(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        return Math.max(simpleRob(nums, 2, nums.length-2)+nums[0], simpleRob(nums, 1, nums.length-1));
    }
    
    /* Recursion Function: f(nums, start, end) = max(f(nums, start+2, end)+nums[start], f(nums, start+1, end)) */
    public int simpleRob(int[] nums, int start, int end) {
        if (end < start) {
            return 0;
        } else {
            int second = 0;
            int first = nums[end];
            // Recursion by DP. ONLY USE O(1) SPACE!
            int pos = end - start - 1;
            while (pos >= 0) {
                // Move forward 2 houses each time
                // Or we can move forward 1 house each time and swap first and second
                second = Math.max(first, nums[start+pos] + second);
                first = Math.max(second, nums[start+pos-1] + first);
                pos -= 2;
            }
            return (pos == -1) ? first : second;
        }
    }
    
    public int simpleRob_On(int[] nums, int start, int end) {
        if (end < start) {
            return 0;
        } else {
            int[] table = new int[end - start + 1 + 1];
            table[end - start + 1] = 0;
            table[end - start] = nums[end];
            // Recursion by DP
            int pos = end - start - 1;
            while (pos >= 0) {
                table[pos] = Math.max((nums[start+pos] + table[pos+2]), table[pos+1]);
                pos --;
            }
            return table[0];
        }
    }
}
