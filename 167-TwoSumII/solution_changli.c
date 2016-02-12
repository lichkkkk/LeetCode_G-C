/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 * 
 * 167. Two Sum II - Input array is sorted
 * Tag: Array
 * Chang Li at UC San Diego
 * Feb. 11, 2016
 */
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    *returnSize = 2;
    int *res = malloc(sizeof(int) * 2);
    int *small = numbers;
    int *big = numbers + numbersSize - 1;
    int sum;
    while ((sum = *small + *big) != target && small < big) {
        if (sum > target) {
            big --;
        } else {
            small ++;
        }
    }
    res[0] = small - numbers + 1;
    res[1] = big - numbers + 1;
    return res;
}
