class Solution:

  def plot_solution(self, n , queens):
    assert n == len(queens)
    solution = [['.'] * n for _ in range(n)]
    for i in range(n):
      solution[i][queens[i]] = 'Q'
    return [''.join(solution[i]) for i in range(n)]

  def placeQueen(self, n, row, col_visited, slash1_visited, slash2_visited, queens, solutions):
    if row == n:
      solutions.append(self.plot_solution(n, queens))
      return
    for col in range(n):
      slash1 = n - row + col -1
      slash2 = row + col
      if col_visited[col] or slash1_visited[slash1] or slash2_visited[slash2]:
        continue
      col_visited[col] = True
      slash1_visited[slash1] = True
      slash2_visited[slash2] = True
      queens.append(col)
      self.placeQueen(n, row + 1, col_visited, slash1_visited, slash2_visited, queens, solutions)
      queens.pop()
      col_visited[col] = False
      slash1_visited[slash1] = False
      slash2_visited[slash2] = False

  def solveNQueens(self, n: int) -> List[List[str]]:
    col_visited = [False] * n
    slash1_visited = [False] * (2*n -1)
    slash2_visited = [False] * (2*n -1)

    solutions = []
    queens = []
    row = 0

    self.placeQueen(n, row, col_visited, slash1_visited, slash2_visited, queens, solutions)

    return solutions
