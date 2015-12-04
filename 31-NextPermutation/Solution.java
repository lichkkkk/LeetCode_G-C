/*
 *  1,2,3 → 1,3,2
 *  3,2,1 → 1,2,3
 *  1,1,5 → 1,5,1
 *
 * Rule: lowest -> increasing highest -> decreasing
 * 1 2 3 4 -> 1 2 4 3 -> 1 3 2 4 -> 1 3 4 2 -> 1 4 2 3
 * 
 * [1] start from length 2, until we found a not highest order sequence or reach the head
 * [2] for a sequence not in highest order, put the next bigger element in the place and reverse
 * [3] complexity : O(n) + O(n)
 * [4] corner case: numbers may be not distinct;
 *
 * Chang Li Dec.4, 2015 at UC San Diego
 *
 */
public class Solution {
    public void nextPermutation(int[] nums) {
        if(nums == null || nums.length <= 1) {
            return;
        }
        // Find the "peak" element
        int pos = nums.length-1;
        while(pos > 0 && nums[pos] <= nums[pos-1]) {
            pos--;
        }
        // If not the highest
        if(pos != 0) {
            // Find the next bigger
            int nextBigger = pos;
            while(nextBigger < nums.length-1 && nums[nextBigger+1] > nums[pos-1]) {
                nextBigger++;
            }
            int temp = nums[nextBigger];
            nums[nextBigger] = nums[pos-1];
            nums[pos-1] = temp;
        }
        // Reverse
        int left = pos;
        int right = nums.length-1;
        while(left < right) {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left ++;
            right --;
        }        
    }
}

