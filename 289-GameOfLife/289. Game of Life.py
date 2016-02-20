__author__ = 'liuxiyun'
# Use 0~3 to store the previous stage and cur stage:
# 0,2 are "dead", and "dead->live" 1,3 are "live", and "live->dead"

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board == [] or board[0]==[]:
            return
        self.m = len(board)
        self.n = len(board[0])
        self.board = board
        for i in range(0,self.m):
            for j in range(0,self.n):
                count_life = self.count_neighbour(i,j)
                # print count_life
                if self.board[i][j]%2==1:
                    if count_life<2 or count_life > 3:
                        self.board[i][j]=3
                else:
                    if count_life ==3:
                        self.board[i][j]= 2
        for i in range(0,self.m):
            for j in range(0,self.n):
                if self.board[i][j] ==3:
                    self.board[i][j] = 0
                if self.board[i][j] == 2:
                    self.board[i][j] = 1

    def count_neighbour(self,i,j):
        count = 0
        if i>0:
            if j>0:
                count+=self.board[i-1][j-1]%2
            count+=self.board[i-1][j]%2
            if j<self.n-1:
                count += self.board[i-1][j+1]%2
        if j>0:
            count +=self.board[i][j-1]%2
        if j<self.n-1:
            count +=self.board[i][j+1]%2
        if i<self.m-1:
            if j>0:
                count += self.board[i+1][j-1]%2
            count+=self.board[i+1][j]%2
            if j<self.n-1:
                count+=self.board[i+1][j+1]%2

        return count
c = Solution()
c.gameOfLife([[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]])