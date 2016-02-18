/**
 * 81. Search in Rotated Sorted Array II
 * Tag: Array, Binary Search
 * Chang Li at UC San Diego
 * Feb. 18, 2016
 */

bool search(int* nums, int numsSize, int target) {
    // Input Check
    if (numsSize <= 0 || nums == NULL) return false;
    // Check Two Sides
    int left = nums[0];
    int right = nums[numsSize-1];
    if (left == target || right == target) return true;
    // Binary Search
    if (left == right) {
        // Equal, can judge
        return search(nums+1, numsSize-2, target);
    } else if (left < right) {
        // In Order
        int mid = nums[numsSize/2];
        if (mid == target) return true;
        else if (mid < target) return search(nums+numsSize/2+1, numsSize-numsSize/2-2, target);
        else return search(nums+1, numsSize-numsSize/2-1, target);
    } else {
        // Rotated Order
        int mid = nums[numsSize/2];
        if (mid == target) {
            return true;
        } else if (mid >= left) {
            if (target < mid && target > left) {
                return search(nums+1, numsSize-numsSize/2-1, target);
            } else {
                return search(nums+numsSize/2+1, numsSize-numsSize/2-2, target);
            }
        } else {
            if (target > mid && target < right) {
                return search(nums+numsSize/2+1, numsSize-numsSize/2-2, target);
            } else {
                return search(nums+1, numsSize-numsSize/2-1, target);
            }
        }
    }
}
