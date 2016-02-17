/**
 * 41. First Missing Positive
 * Chang Li at UC San Diego
 */
 
public class Solution {
    public int firstMissingPositive(int[] nums) {
        // You definitely need to store the search infomation
        // And the information is in O(n). Now that you can not use additional space
        // Try to use the array itself to store this information
        if(nums == null) {
            return 1;
        }
        for(int i=0; i<nums.length; i++) {
            while(nums[i] > 0 && nums[i] <= nums.length && nums[i] != i+1) {
                int temp = nums[nums[i]-1];
                // This if-branch is necessary, or it will lead to an infinite loop
                if(temp == nums[i]) {
                    break;
                }
                nums[nums[i]-1] = nums[i];
                nums[i] = temp;
            }
        }
        // Because we will swap at most N times and the array's length is N, so the total complexity is O(n)
        
        for(int i=0; i<nums.length; i++) {
            if(nums[i] != i+1) {
                return i+1;
            }
        }
        return nums.length+1;
    }
}