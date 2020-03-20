class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # find the first negative number in the bottom row
        x, y = len(grid) - 1, 0
        while y < len(grid[0]) and grid[x][y] >= 0:
            y += 1

        # count row by row, bottom to top
        total = 0
        while x >= 0 and y < len(grid[0]):
            total += len(grid[0]) - y
            x -= 1
            if x < 0:
                break
            while y < len(grid[0]) and grid[x][y] >= 0:
                y += 1
        
        return total
