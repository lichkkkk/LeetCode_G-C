/*
 * Slightly modify the 3-SUM solution and then get the follow answer.
 *
 * Running Time: O(n^2)
 * Chang Li at UC San Diego
 * Dec. 9, 2015
 */

public class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        int count = 0;
        Arrays.sort(nums);
        for(int i=0; i<nums.length-2; i++) {
            int left = i+1;
            int right = nums.length-1;
            while(left < right) {
                while(right > left && nums[i] + nums[left] + nums[right] >= target) {
                    right --;
                }
                count += right - left;
                left ++;
            }
        }
        return count;
    }
}
