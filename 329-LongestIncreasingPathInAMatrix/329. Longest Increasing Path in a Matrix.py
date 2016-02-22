__author__ = 'liuxiyun'
# DFS
# The trick is to memorize
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if matrix == [] or matrix == [[]]:
            return 0
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrix=matrix
        self.max_len = [[0 for r in range(self.n)]for s in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                self.explore(i,j)
        return max(x for room in self.max_len for x in room)

    def explore(self,i,j):
        if self.max_len[i][j]!=0: # If already explored, no need to explore again.
            return self.max_len[i][j]

        if i>0 and self.matrix[i][j]<self.matrix[i-1][j]:
            up = self.explore(i-1,j)+1
        else:
            up = 1

        if j>0 and self.matrix[i][j]<self.matrix[i][j-1]:
            left = self.explore(i,j-1)+1
        else:
            left = 1

        if i<self.m-1 and self.matrix[i][j]<self.matrix[i+1][j]:
            down = self.explore(i+1,j)+1
        else:
            down = 1

        if j<self.n-1 and self.matrix[i][j]<self.matrix[i][j+1]:
            right = self.explore(i,j+1)+1
        else:
            right = 1

        self.max_len[i][j] = max(up,down,left,right)
        return self.max_len[i][j]
