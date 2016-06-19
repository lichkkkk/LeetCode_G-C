/**
 * 361. Bomb Enemy
 * Brute Force: For each empty cell, check its row and column, O(m*n*(m+n))
 * DP: For wach cell, store the enemy can kiil in 4 directions, Time : O(m*n), Space O(m*n)
 * Better DP: Two Table, one for right down, one for left up, O(m*n)
 * 
 * Better solutions exist, but ony with some small improment.
 *
 * Chang Li @ Mountain View
 * Jun. 18, 2016
 */
public class Solution {
    public int maxKilledEnemies(char[][] grid) {
        if (grid.length == 0 || grid[0].length == 0) {
            return 0;
        }
        int rowLen = grid.length;
        int colLen = grid[0].length;
        int[][] right = new int[rowLen][colLen];
        int[][] left = new int[rowLen][colLen];
        int[][] down = new int[rowLen][colLen];
        int[][] up = new int[rowLen][colLen];
        
        // Filling tables
        for (int i=rowLen-1; i>=0; i--) {
            right[i][colLen-1] = grid[i][colLen-1] == 'E' ? 1 : 0;
            for (int j=colLen-2; j>=0; j--) {
                // If meet the wall
                if (grid[i][j] == 'W') {
                    right[i][j] = 0;
                }
                // Else, compute the number of enemy can be killed in that two directions
                else {
                    right[i][j] = right[i][j+1] + (grid[i][j] == 'E' ? 1 : 0);
                }
            }
        }
        for (int j=colLen-1; j>=0; j--) {
            down[rowLen-1][j] = grid[rowLen-1][j] == 'E' ? 1 : 0;
            for (int i=rowLen-2; i>=0; i--) {
                // If meet the wall
                if (grid[i][j] == 'W') {
                    down[i][j] = 0;
                }
                // Else, compute the number of enemy can be killed in that two directions
                else {
                    down[i][j] = down[i+1][j] + (grid[i][j] == 'E' ? 1 : 0);
                }
            }
        }
        for (int i=0; i<rowLen; i++) {
            left[i][0] = grid[i][0] == 'E' ? 1 : 0;
            for (int j=1; j<colLen; j++) {
                // If meet the wall
                if (grid[i][j] == 'W') {
                    left[i][j] = 0;
                }
                // Else, compute the number of enemy can be killed in that two directions
                else {
                    left[i][j] = left[i][j-1] + (grid[i][j] == 'E' ? 1 : 0);
                }
            }
        }
        // Fill left up table and find the result meanwhile
        for (int j=0; j<colLen; j++) {
            up[0][j] = grid[0][j] == 'E' ? 1 : 0;
            for (int i=1; i<rowLen; i++) {
                // If meet the wall
                if (grid[i][j] == 'W') {
                    up[i][j] = 0;
                }
                // Else, compute the number of enemy can be killed in that two directions
                else {
                    up[i][j] = up[i-1][j] + (grid[i][j] == 'E' ? 1 : 0);
                }
            }
        }
        
        int biggest = 0;
        for (int i=0; i<rowLen; i++) {
            for (int j=0; j<colLen; j++) {
                int currKillNum = left[i][j] + right[i][j] + up[i][j] + down[i][j];
                if (grid[i][j] == '0' && currKillNum > biggest) {
                    biggest = currKillNum;
                }
            }
        }
        //printTable(up);
        return biggest;
    }
    
    public void printTable(int[][] table) {
        int iLen = table.length;
        int jLen = table[0].length;
        for (int i=0; i<iLen; i++) {
            for (int j=0; j<jLen; j++) {
                System.out.print(table[i][j] + " ");
            }
            System.out.println();
        }
    }
}
