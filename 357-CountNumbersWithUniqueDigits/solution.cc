/**
 * 357. Count Numbers with Unique Digits
 * 
 * Chang Li @ Mountain View
 * Jul. 5, 2016
 */
class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        if (n == 0) {
            return 1;
        } else if (n > 10) {
            return 0;
        } else {
            int sum = 9;
            for (int i=0; i<n-1; ++i) {
                sum *= (9 - i);
            }
            return sum + countNumbersWithUniqueDigits(n-1);
        }
    }
};
