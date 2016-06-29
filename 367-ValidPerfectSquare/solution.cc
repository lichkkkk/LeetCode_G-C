/**
 * 367. Valid Perfect Square
 *      Cost 0ms :-D
 * Chang Li @ Mountain View
 * Jun. 28, 2016
 */

class Solution {
public:
    bool isPerfectSquare(int num) {
        int rt = root(num);
        return rt*rt == num;
    }
    
    int root(int num) {
        int rt = 2;
        while (true) {
            int div_res = num/rt;
            if (div_res == rt) {
                return rt;
            } else if (div_res < rt) {
                return rt - 1;
            } else {
                int step = root(div_res/rt);
                rt = (step>1) ? rt*step : rt+1;
            }
        }
    }
};
