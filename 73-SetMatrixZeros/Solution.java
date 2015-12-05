/*
 * If you are required to use constant memory space to store an 
 * information that related to the size of this problem, like in
 * this problem, a possible way is to utilize the spzec in the 
 * parameters, like the given matrix in this problem.
 *
 * It's not easy to find out all of the corner cases.
 * Running Time: Time:O(n^2) Space:O(1)
 *
 * Chang Li at UC San Diego
 * Dec. 4, 2015
 */

public class Solution {
    public void setZeroes(int[][] matrix) {
 		
		if(matrix == null || matrix.length == 0 || matrix[0].length ==0) {
			return;
		}
		
		int firstLine = 1;
		
		for(int j=0; j<matrix.length; j++) {
			if(matrix[j][0] == 0) {
				firstLine = 0;
				break;
			}
		}
		
		for(int i=0; i<matrix.length; i++) {
			for(int j=1; j<matrix[0].length; j++) {
				if(matrix[i][j] == 0) {
					matrix[i][0] = 0;
					matrix[0][j] = 0;
				}
			}
		}

		for(int i=1; i<matrix.length; i++) {
			for(int j=1; j<matrix[0].length; j++) {
				if(matrix[i][0] == 0 || matrix[0][j] == 0) {
					matrix[i][j] = 0;
				}
			}
		}

		if(matrix[0][0] == 0) {
			for(int i=0; i<matrix[0].length; i++) {
				matrix[0][i] = 0;
			}
		}

		if(firstLine == 0) {
			for(int i=0; i<matrix.length; i++) {
				matrix[i][0] = 0;
			}
		}
    }
}
