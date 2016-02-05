    # 37. Sudoku Solver
# Tag: 2D-Array
#       Brute-Force
#       Use three lists to maintain the number appeard in each row, wach column and each block
#       Use another list to store cells to be filled
# Running Time: O(n^2) + O(n^2) * O(n^2) (? Not sure)
# Chang Li at UC San Diego
# Jan. 5, 2016

class Solution(object):

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead
        """
        candidates = [[['1','2','3','4','5','6','7','8','9'] for x in range(9)] for y in range(9)]
        to_do_list = []

        """Initialize: Read Info From Board"""
        for ind_row in range(9):
            for ind_col in range(9):
                num = board[ind_row][ind_col]
                if num != '.':
                    candidates[ind_row][ind_col] = []
                    self.updateCandidates(num, ind_row, ind_col, candidates, to_do_list)
                else:
                    continue

        """Keep Filling"""
        if not self.helper(board, candidates, to_do_list):
            print "No Feasible Solution"

    def helper(self, board, candidates, to_do_list):
        """Fill"""
        while len(to_do_list) > 0:
            (ind_row, ind_col, num) = to_do_list.pop()
            if not self.isAvailable(num, ind_row, ind_col, board):
                print "Invalid Input"
                return False
            board[ind_row] = board[ind_row][:ind_col] + [num] + board[ind_row][ind_col+1:]
            candidates[ind_row][ind_col] = []
            self.updateCandidates(num, ind_row, ind_col, candidates, to_do_list)

        """Guess"""
        board_backup = copy.deepcopy(board)
        candidates_backup = copy.deepcopy(candidates)
        """Find the cell has least candidates to speed up the search"""
        min_candidates_set =(-1, -1, 10)
        for ind_row in range(9):
            for ind_col in range(9):
                num = board[ind_row][ind_col]
                if num == '.' and len(candidates[ind_row][ind_col]) > 0 \
                                and len(candidates[ind_row][ind_col]) < min_candidates_set[2]:
                    min_candidates_set = (ind_row, ind_col, len(candidates[ind_row][ind_col]))
        """If all cells have been filled, return true"""
        if min_candidates_set[2] == 10:
            return True
        """Make a guess, then move forward"""
        ind_row = min_candidates_set[0]
        ind_col = min_candidates_set[1]
        for candidate in candidates[ind_row][ind_col]:
            to_do_list = [(ind_row, ind_col, candidate)]
            if self.helper(board,candidates,to_do_list):
                return True
            else:
                """If we found the guess was wrong, roll back and try another guess"""
                for ind in range(9):
                    board[ind] = copy.deepcopy(board_backup[ind])
                candidates = copy.deepcopy(candidates_backup)
        return False

    def updateCandidates(self, num, ind_row, ind_col, candidates, to_do_list):
        """After fill one cell, update to see if another cell can be filled"""
        """Update Each Row"""
        for row in range(9):
            lst = candidates[row][ind_col]
            if num in lst:
                lst.remove(num)
            if len(lst) == 1:
                to_do_list.append((row, ind_col, lst.pop()))

        """Update Each Column"""
        for col in range(9):
            lst = candidates[ind_row][col]
            if num in lst:
                lst.remove(num)
            if len(lst) == 1:
                to_do_list.append((ind_row, col, lst.pop()))

        """Update Each Block"""
        row_base = (ind_row/3)*3
        col_base = (ind_col/3)*3
        for row in range(row_base, row_base+3):
            for col in range(col_base, col_base+3):
                lst = candidates[row][col]
                if num in lst:
                    lst.remove(num)
                if len(lst) == 1:
                    to_do_list.append((row, col, lst.pop()))


    def isAvailable(self, num, ind_row, ind_col, board):
        """Because somethimes we guess, so some conflicts may occur, 
            which indicates the previous guess was wrong"""
        if num in board[ind_row]:
            return False
        for i in range(9):
            if num in board[i][ind_col]:
                return False
        row_base = (ind_row/3)*3
        col_base = (ind_col/3)*3
        for row in range(row_base, row_base+3):
            for col in range(col_base, col_base+3):
                if num in board[row][col]:
                    return False
        return True