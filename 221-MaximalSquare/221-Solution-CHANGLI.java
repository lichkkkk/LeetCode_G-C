/**
 * 221. Maximal Square
 * Tag: 2D-Array, DP
 *      The core to solve this problem is HOW to "detect" a square. Graph search can do
 *      this, but looks too dumb. On the contrast, making judgments according to the adjacent
 *      cells is much better.
 * Chang Li at UC San Diego
 * Jan. 26, 2016
 */
 
public class Solution {
    public int maximalSquare(char[][] matrix) {
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        int [][] table = new int[matrix.length][matrix[0].length];
        int max = 0;
        for(int i=0; i<matrix.length; i++) {
            for(int j=0; j<matrix[0].length; j++) {
                if(i == 0 || j == 0 || matrix[i][j] == '0') {
                    table[i][j] = matrix[i][j] - '0';
                }else {
                    table[i][j] = Math.min(Math.min(table[i-1][j], table[i][j-1]), table[i-1][j-1]) + 1;
                }
                max = Math.max(max, table[i][j]);
            }
        }
        return max*max;
    }
}
