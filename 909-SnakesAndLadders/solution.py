class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
      n = len(board)
      board_visited = set([1])
      label_queue = [1]
      steps = 0
      while label_queue:
        next_label_queue = []
        for label in label_queue:
          if label == n**2:
            return steps
          else:
            next_labels = self.getNextLabels(board, board_visited, label)
            next_label_queue.extend(next_labels)
        label_queue = next_label_queue
        steps += 1
      return -1

    def getNextLabels(self, board: List[List[int]], label_visited: Set[int], curr_label: int) -> List[int]:
      n = len(board)
      all_next_labels = [curr_label + i for i in range(1, 7)]
      valid_next_labels = []
      for label in all_next_labels:
        if label > n**2:
          continue
        label_value_on_board = self.getLabelValueOnBoard(board, label)
        if label_value_on_board != -1:
          label = label_value_on_board
        if label in label_visited:
          continue
        valid_next_labels.append(label)
        label_visited.add(label)
      return valid_next_labels

    def getLabelValueOnBoard(self, board: List[List[int]], label: int) -> List[int]:
      n = len(board)
      assert 1 <= label <=  n**2
      row = n - 1 - (label - 1) // n
      col = (label - 1) % n
      if (n - row) % 2 == 0:
        col = n - col - 1
      return board[row][col]
