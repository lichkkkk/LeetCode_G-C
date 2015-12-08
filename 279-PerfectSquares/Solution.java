/*
 * Classic Knapsack Problem.
 * Use One-Dimision DP to solve.
 *
 * Running Time: O(n^1.5)
 * Chang Li at UC San Diego
 * Dec. 7, 2015
 */

public class Solution {
    public int numSquares(int n) {
        int[] table = new int[n+1];
        // F(n) = min (F(n-k*k) + 1)
        table[1] = 1;
        for(int i=1; i<=n; i++) {
            int min = n;
            for(int j=1; j*j<=i; j++) {
                min = Math.min(min, table[i-j*j] + 1);
            }
            table[i] = min;
        }
        return table[n];
    }
}
