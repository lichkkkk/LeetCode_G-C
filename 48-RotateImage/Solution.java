/*
 * Rotate an image by 90 degree. Implemented by two loops.
 * Running Time: O(n)
 * Like a longer "Exchange Value", just be careful of the index
 * Chang Li at UC San Diego
 * Dec. 4, 2015
 */
public class Solution {
    public void rotate(int[][] matrix) {
    	if(matrix == null || matrix.length == 0 || matrix[0].length == 0) {
		return;
	}
	int layer = matrix.length;
	int step = matrix.length - 1;
	while(step >= 1) {
		int x = layer-1;
		int y = layer-1;
		for(int i=0; i<step; i++) {
    		int tmp = matrix[y-i][x];
    		matrix[y-i][x] = matrix[y-step][x-i];
    		matrix[y-step][x-i] = matrix[y-step+i][x-step];
    		matrix[y-step+i][x-step] = matrix[y][x-step+i];
    		matrix[y][x-step+i] = tmp;
		}
		layer-=1;
		step-=2;
    }
    }
}
