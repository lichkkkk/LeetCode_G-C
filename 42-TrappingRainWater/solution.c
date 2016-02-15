/**
 * 42. Trapping Rain Water
 * Tag: Array, Two Pointers
 * Running Time: O(n)
 * Chang Li at UC San Diego
 * Feb. 14, 2016
 */

int trap(int* height, int heightSize) {
    
    if (heightSize <= 1) return 0;
    
    int left = 0;
    int right = heightSize - 1;
    int base = 0;
    int totalSpace = 0;
    int occupiedSpace = 0;
    
    while (right != left) {
        if (height[right] >= height[left]) {
            while (right != left && height[left] <= base) {
                occupiedSpace += height[left];
                left ++;
            }
        } else {
            while (right != left && height[right] <= base) {
                occupiedSpace += height[right];
                right --;
            }
        }
        totalSpace += (min(height[right], height[left]) - base) * (right - left + 1);
        base = min(height[right], height[left]);
    }
    occupiedSpace += height[right];
    return totalSpace - occupiedSpace;
}

int min(int a, int b) {
    if (a >=b) return b;
    else return a;
}
