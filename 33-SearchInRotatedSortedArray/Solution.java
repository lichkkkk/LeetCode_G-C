/*
 * Nothing special, just Binary Search.
 * The boundary conditions are really suffering.
 *
 * Running Time: O(logN)
 *
 * Chang Li at UC San Diego
 * Dec. 4, 2015
 */

public class Solution {
    public int search(int[] nums, int target) {
        return helper(nums, 0, nums.length-1, target);
    }
    
    public int helper(int[] nums, int start, int end, int target) {
        if(start > end) {
            return -1;
        }
        if(start == end) {
            if(nums[start] == target) {
                return start;
            }else {
                return -1;
            }
        }
        int mid = start + (end - start) / 2;
        if(nums[start] < nums[end]) {
            if(nums[mid] == target) {
                return mid;
            }else if(nums[mid] > target) {
                return helper(nums, start, mid-1, target);
            }else {
                return helper(nums, mid+1, end, target);
            }
        }else {
            if(nums[mid] == target) {
                return mid;
            }
            if(nums[mid] >= nums[start]) {
                if(nums[mid] > target && target >= nums[start]) {
                    return helper(nums, start, mid-1, target);    
                }else {
                    return helper(nums, mid+1, end, target);  
                }
            }else {
                if(nums[mid] < target && target <= nums[end]) {
                    return helper(nums, mid+1, end, target);    
                }else {
                    return helper(nums, start, mid-1, target);  
                }
            }
        }
    }
}
