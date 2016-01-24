__author__ = 'liuxiyun'

# My idea is depth first search. Everytime meet a new land, explore it and # of island +1
# # Scan each cell in the grid.
# # If the cell value is '1' explore that island.
# # Mark the explored island cells with 'visited'.
# # Once finished exploring that island, increment islands counter.

# Time: O(m*n) // explore calls O(m*n) times
# Space: O(m*n)
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []:
            return 0
        self.row = len(grid)
        self.col = len(grid[0])
        island = 0
        self.label = [['unvisited' for j in range(self.col)] for i in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                if self.label[i][j] == 'visited':
                    continue
                if grid[i][j]=='1':
                    self.explore(grid,i,j)
                    island+=1
        return island

    def explore(self,grid,i,j):  # O(1)
        self.label[i][j] = 'visited'
        if i-1>=0 and grid[i-1][j] == '1' and self.label[i-1][j] == 'unvisited':
            self.explore(grid,i-1,j)
        if j-1>=0 and grid[i][j-1] == '1' and self.label[i][j-1] == 'unvisited':
            self.explore(grid,i,j-1)
        if i+1<self.row and grid[i+1][j] == '1' and self.label[i+1][j] == 'unvisited':
            self.explore(grid,i+1,j)
        if j+1<self.col and grid[i][j+1] == '1'and self.label[i][j+1] == 'unvisited':
            self.explore(grid,i,j+1)
        return

# Test case:
# # []
# # ['1']
# # ['0']
# # ['11']
# # one island
# # no island
# # more than one island and need to explore