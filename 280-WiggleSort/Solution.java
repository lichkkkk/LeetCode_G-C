/*
 * This version is very concise.
 * The easiest way is to sort the array first. But actually it is
 * unnecessary. We assume the part before the pointer has already 
 * satisfied the requirement.
 * 
 * Running Time: O(n)
 * Chang Li at UC San Diego
 * Dec. 8, 2015
 */

public class Solution {
    public void wiggleSort(int[] nums) {
        for(int i=1; i<nums.length; i++) {
            if((i%2)==1 == nums[i]<nums[i-1]) {
                int tmp = nums[i];
                nums[i] = nums[i-1];
                nums[i-1] = tmp;
            }
        }
    }
}
