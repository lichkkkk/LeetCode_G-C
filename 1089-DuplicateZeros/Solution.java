/**
 * 1089. Duplicate Zeros
 * Jun. 25, 2019 50 Columbus, Jersey City
 */
class Solution {
    public void duplicateZeros(int[] arr) {
        if (arr == null || arr.length <= 1) {
            return;
        }
        int left = 0;
        int right = arr.length-1;
        while (left < right) {
            if (arr[left] == 0) {
                right--;
            }
            left++;
        }
        int i = arr.length - 1;
        // Corner case: last 0 not duplicated
        if (left == right && arr[left] == 0) {
            arr[i] = 0;
            i--;
            right--;
        }
        while (i >= 0) {
            if (arr[right] == 0) {
                arr[i] = 0;
                i--;
            }
            arr[i] = arr[right];
            i--;
            right--;
        }
    }
}
