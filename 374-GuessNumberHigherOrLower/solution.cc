// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

/**
 * 374. Guess Number Higher or Lower
 * 
 * Chang Li @ Mountain view
 * Jul. 12, 2016
 */
class Solution {
public:
    int guessNumber(int n) {
        int min = 1;
        int max = n;
        while (min + 1 < max) {
            int mid = min + (max - min) / 2;
            int feedback = guess(mid);
            if (feedback > 0) {
                min = mid + 1;
            } else if (feedback == 0) {
                return mid;
            } else {
                max = mid - 1;
            }
        }
        if (guess(max)) return min;
        else return max;
    }
};
