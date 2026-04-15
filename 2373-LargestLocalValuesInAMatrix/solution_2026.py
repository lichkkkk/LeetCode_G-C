class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        x, y = len(grid), len(grid[0])
        res = [[0] * (y-2) for _ in range(x-2)]
        for i in range(1, x-1):
            for j in range(1, y-1):
                res[i-1][j-1] = max(grid[i-1][j-1:j+2] + grid[i][j-1:j+2] + grid[i+1][j-1:j+2])
        return res
