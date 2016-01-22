/**
 * 329. Longest Increasing Path in a Matrix
 * Tag: DFS, DP
 * Chang Li at UC San Diego
 * Jan. 21, 2016
 */

public class Solution {
    public int longestIncreasingPath(int[][] matrix) {
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        int[][] table = new int[matrix.length][matrix[0].length];
        int maxLen = 0;
        for(int i=0; i<matrix.length; i++) {
            for(int j=0; j<matrix[0].length; j++) {
                maxLen = Math.max(maxLen, DFS(matrix, i, j, table));
            }
        }
        return maxLen;
    }
    
    public int DFS(int[][] matrix, int x, int y, int[][] table) {
        if(table[x][y] != 0) {
            return table[x][y];
        }
        int maxLen = 1;
        if(x != 0 && matrix[x-1][y] > matrix[x][y]) {
            maxLen = Math.max(maxLen, 1+DFS(matrix, x-1, y, table));
        }
        if(x != matrix.length-1 && matrix[x+1][y] > matrix[x][y]) {
            maxLen = Math.max(maxLen, 1+DFS(matrix, x+1, y, table));
        }
        if(y != 0 && matrix[x][y-1] > matrix[x][y]) {
            maxLen = Math.max(maxLen, 1+DFS(matrix, x, y-1, table));
        }
        if(y != matrix[0].length-1 && matrix[x][y+1] > matrix[x][y]) {
            maxLen = Math.max(maxLen, 1+DFS(matrix, x, y+1, table));
        }
        table[x][y] = maxLen;
        return maxLen;
    }
}