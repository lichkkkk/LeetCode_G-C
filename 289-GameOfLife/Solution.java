// 3: Live to Live
// 2: Dead to Live
// 1: Live to Dead
// 0: Dead to Dead
// v mod 2 = original state
// v div 2 = new state
//
// Chang Li at UC San Diego
// Dec. 5, 2015

public class Solution {
    public void gameOfLife(int[][] board) {
        if(board == null || board.length == 0 || board[0].length == 0) {
            return;
        }
        for(int i=0; i<board.length; i++) {
            for(int j=0; j<board[0].length; j++) {
                board[i][j] = getNewState(board, i, j);
            }
        }
        for(int i=0; i<board.length; i++) {
            for(int j=0; j<board[0].length; j++) {
                board[i][j] /= 2;
            }
        }
    }
    
    public int getNewState(int[][] board, int i, int j) {
        int alive = state(board, i-1, j-1) + state(board, i-1, j) + state(board, i-1, j+1) +
                    state(board, i  , j-1)                        + state(board, i  , j+1) +
                    state(board, i+1, j-1) + state(board, i+1, j) + state(board, i+1, j+1);
        int originalState = board[i][j];
        if(originalState == 1) {
            if(alive < 2 || alive > 3) {
                return 1;
            }else {
                return 3;
            }
        }else {
            if(alive == 3) {
                return 2;
            }else {
                return 0;
            }
        }
    }
    
    public int state(int[][] board, int i, int j) {
        if(i < 0 || j < 0 || i >= board.length || j >= board[0].length) {
            return 0;
        }else {
            return board[i][j] % 2;
        }
    }
}
