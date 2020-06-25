class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
      size = len(grid)
      if size == 0 or grid[0][0] != 0 or grid[size-1][size-1] != 0:
        return -1
      dq = deque()
      dq.append((0,0))
      grid[0][0] = 1
      steps = 0
      while len(dq) != 0:
        steps += 1
        for _ in range(len(dq)):
          pos = dq.popleft()
          if pos[0] == size-1 and pos[1] == size-1:
            return steps
          else:
            for adj_pos in self.get_adj_pos(grid, pos):
              dq.append(adj_pos)
              grid[adj_pos[0]][adj_pos[1]] = 1
      return -1
    
    def get_adj_pos(self, grid, pos):
      offsets = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
      size = len(grid)
      res = []
      for offset in offsets:
        p0 = offset[0] + pos[0]
        p1 = offset[1] + pos[1]
        if 0 <= p0 < size and 0 <= p1 < size and grid[p0][p1] == 0:
          res.append((p0, p1))
      return res
