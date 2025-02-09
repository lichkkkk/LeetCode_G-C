class Solution:
    def get_adj_pos(self, i: int, j: int, mat: List[List[int]]) -> List[List[int]]:
      res = []
      for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_i, new_j = i + di, j + dj
        if (0 <= new_i < len(mat)) and (0 <= new_j < len(mat[0])):
          res.append((new_i, new_j))
      return res
   
    def _helper(self, i: int, j: int, states: List[List[int]], matrix: List[List[int]]) -> int:
      if states[i][j] != 0:
        return states[i][j]
      longest = 0
      for new_i, new_j in self.get_adj_pos(i, j, matrix):
        if matrix[new_i][new_j] > matrix[i][j]:
          longest = max(longest, self._helper(new_i, new_j, states, matrix))
      states[i][j] = longest + 1
      return states[i][j]

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
      states = [[0] * len(matrix[0]) for _ in range(len(matrix))]
      res = 0
      for i in range(len(matrix)):
        for j in range(len(matrix[0])):
          res = max(res, self._helper(i, j, states, matrix))

      # for i in range(len(matrix)):
      #   print(states[i])

      return res
