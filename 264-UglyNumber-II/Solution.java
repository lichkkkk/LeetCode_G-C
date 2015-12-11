/*
 * For this question, it's obvious we have to generate new numbers based
 * on previous numbers. So it is a good idea to store all numbers in an
 * array. Then, we noticed that there are three ways to get a new number:
 * multiply 2, multiply 3, multiply 5. So we need to maintain three 
 * pointers to know which numbers can be used as base.
 *
 * The code is not mine, but is really concise and beautiful.
 * Runnning Time: O(n)
 *
 * Chang Li at UC San Diego
 * Dec, 10, 2015
 */

public class Solution {
    public int nthUglyNumber(int n) {
        int[] k = new int[n];
        k[0] = 1;
        int ind2 = 0;
        int ind3 = 0;
        int ind5 = 0;
        for(int i=1; i<n; i++) {
            int min = Math.min(k[ind2] * 2, Math.min(k[ind3]*3, k[ind5]*5));
            k[i] = min;
            if(k[i] % 2 == 0) ind2++;
            if(k[i] % 3 == 0) ind3++;
            if(k[i] % 5 == 0) ind5++;
        }
        return k[n-1];
    }
}
