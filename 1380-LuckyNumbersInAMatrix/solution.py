class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
      if len(matrix) == 0 or len(matrix[0]) == 0:
        return []
      
      col_max = []
      for j in range(len(matrix[0])):
        curr_col_max = matrix[0][j]
        for i in range(1, len(matrix)):
          curr_col_max = max(curr_col_max, matrix[i][j])
        col_max.append(curr_col_max)
      
      res = []
      for i in range(len(matrix)):
        row_min = min(matrix[i])
        for j in range(len(matrix[0])):
          if matrix[i][j] == row_min and row_min == col_max[j]:
            res.append(matrix[i][j])
      
      return res
