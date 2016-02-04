/**
 * 174. Dungeon Game
 * Tag: Dynamic Programming
 * Chang Li at UC San Diego
 * Feb. 4, 2016
 */

public class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        // Input Check
        if (dungeon == null || dungeon.length == 0 || dungeon[0].length == 0) {
            return -1;
        }
        // DP vector
        int height = dungeon.length;
        int width = dungeon[0].length;
        int[] vector = new int[width];
        // Initizlize DP Vector according to the bottom line
        vector[width - 1] = Math.max(1, 1-dungeon[height-1][width-1]);
        for (int j=width-2; j>=0; j--) {
            vector[j] = Math.max(1, vector[j+1] - dungeon[height-1][j]);
        }
        // DP from bottom right to top left
        for (int i=height-2; i>=0; i--) {
            vector[width-1] = Math.max(1, vector[width-1] - dungeon[i][width-1]);
            for (int j=width-2; j>=0; j--) {
                vector[j] = Math.min(Math.max(1, vector[j]-dungeon[i][j]),
                                    Math.max(1, vector[j+1]-dungeon[i][j]));
            }
        }
        // Vector[0] represents the start position
        return vector[0];
    }
}
