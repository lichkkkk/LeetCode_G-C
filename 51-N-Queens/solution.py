class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        curr_pos = []
        board = [[0] * n for _ in range(n)]
        
        self.place(res, n, curr_pos, board)
        
        str_res = []
        template = ["."] * n
        for poses in res:
            new_res = []
            for p in poses:
                template[p] = "Q"
                new_res.append("".join(template))
                template[p] = "."
            str_res.append(new_res)
        return str_res
    
    def place(self, res, n, curr_pos, board):
        row = len(curr_pos)
        if row == n:
            res.append(curr_pos.copy())
            return
        
        for i in range(n):
            if board[row][i] > 0:
                continue
            
            # Set up
            curr_pos.append(i)
            board[row][i] += 1
            l, r = i - 1, i + 1
            for row_below in range(row+1, n):
                if l >= 0:
                    board[row_below][l] += 1
                    l -= 1
                if r < n:
                    board[row_below][r] += 1
                    r += 1
                board[row_below][i] += 1
            
            # Recursion
            self.place(res, n, curr_pos, board)
            
            # Clean Up
            curr_pos.pop()
            board[row][i] -= 1
            l, r = i - 1, i + 1
            for row_below in range(row+1, n):
                if l >= 0:
                    board[row_below][l] -= 1
                    l -= 1
                if r < n:
                    board[row_below][r] -= 1
                    r += 1
                board[row_below][i] -= 1
                
# There are better ways to remember the Queens placed
