class Solution {
    public int diagonalSum(int[][] mat) {
        int res = 0;
        for (int i=0; i<mat.length; i++) {
            if (i != mat.length-i-1) {
                res += mat[i][i] + mat[i][mat.length-i-1];
            } else {
                res += mat[i][i];
            }
        }
        return res;
    }
}
