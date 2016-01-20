/**
 * 326. Power of Three
 * 
 * Coolest solution I found:
 * 
 *  public boolean isPowerOfThree(int n) {
 *      return n > 0 && (1162261467 % n == 0);
 *  }
 * 
 * where 1162261467 is the max-int-number of power three.
 * 
 * Chang Li at UC San Diego
 * Jan. 19, 2016
 */

public class Solution {
    public boolean isPowerOfThree(int n) {
        long cmp = 1;
        while(cmp < n) cmp = cmp * 3;
        if(cmp == n) return true;
        else return false;
    }
}
