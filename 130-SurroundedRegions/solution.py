class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if len(board) == 0 or len(board[0]) == 0:
            return
        # handle the boarder case
        for i in [0, len(board)-1]:
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    self.fill(board, i, j, 'V')
        for i in range(len(board)):
            for j in [0, len(board[0])-1]:
                if board[i][j] == 'O':
                    self.fill(board, i, j, 'V')            
        # handle the inner space and reset 'V' back to 'O' at the same time
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'V':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
    
    def fill(self, board, i, j, ch):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != 'O':
            return
        board[i][j] = ch
        self.fill(board, i+1, j, ch)
        self.fill(board, i-1, j, ch)
        self.fill(board, i, j+1, ch)
        self.fill(board, i, j-1, ch)
        
# check this: https://leetcode.com/problems/surrounded-regions/discuss/196152/Python-beats-98-easy-to-understand-DFS-solution
