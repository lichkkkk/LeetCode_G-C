"""
Also added additional code to output the optimal path
"""
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
      if len(grid) == 0 or len(grid[0]) == 0:
        return 0
      h, w = len(grid), len(grid[0])
      """
      table[i][j] => (min_sum_from_here, next_direction)
      """
      table = [[(None, None)] * w for _ in range(h)]
      table[0][0] = (grid[0][0], None)
      
      for i in range(h):
        for j in range(w):
          if i == j == 0:
            continue
          elif i == 0:
            table[i][j] = (table[i][j-1][0] + grid[i][j], 'left')
          elif j == 0:
            table[i][j] = (table[i-1][j][0] + grid[i][j], 'up')
          else:
            table[i][j] = (table[i][j-1][0] + grid[i][j], 'left') \
                          if table[i][j-1][0] < table[i-1][j][0] \
                          else (table[i-1][j][0] + grid[i][j], 'up')
      # output the path
      path = []
      curr_node = (h-1, w-1)
      while curr_node != (0, 0):
        path.append(curr_node)
        if table[curr_node[0]][curr_node[1]][1] == 'up':
          curr_node = (curr_node[0]-1, curr_node[1])
        else:
          curr_node = (curr_node[0], curr_node[1]-1)
      path.append((0, 0))
      path.reverse()
      # print(path)
      
      return table[-1][-1][0]
