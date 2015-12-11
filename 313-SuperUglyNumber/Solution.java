/*
 * The idea is the same as Ugly Number -II. Just rewrite with loops.
 *
 * Running Time: O(nk)
 *
 * Chang Li at UC San Diego
 * Dec. 10, 2015
 */

public class Solution {
    public int nthSuperUglyNumber(int n, int[] primes) {
        int[] k = new int[n];
        k[0] = 1;
        int[] ptr = new int[primes.length];
        for(int i=1; i<n; i++) {
            int min = Integer.MAX_VALUE;
            for(int j=0; j<primes.length; j++) {
                min = Math.min(min, primes[j] * k[ptr[j]]);
            }
            k[i] = min;
            for(int j=0; j<primes.length; j++) {
                if(k[i] % primes[j] == 0) {
                    ptr[j] ++;
                }
            }
        }
        return k[n-1];
    }
}
