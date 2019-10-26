/**
 * 1091. Shortest Path in Binary Matrix
 * Jun. 22, 2019 Google NYC
 */
class Solution {
  
    static class Cell {
      int x;
      int y;
      boolean isDummyCell;
      private Cell(int x, int y, boolean isDummyCell) {
        this.x = x;
        this.y = y;
        this.isDummyCell = isDummyCell;
      }
      public static Cell createCell(int x, int y) {
        return new Cell(x, y, false);
      }
      public static Cell createDummy() {
        return new Cell(-1, -1, true);
      }
    }
  
    public int shortestPathBinaryMatrix(int[][] grid) {
        if (grid.length == 0 || grid[0].length == 0) {
          return -1;
        }
        if (grid[0][0] == 1 || grid[grid.length-1][grid[0].length-1] == 1) {
          return -1;
        }
        Queue<Cell> queue = new LinkedList<>();
        int currentDistance = 1;
        queue.add(new Cell(0, 0, false));
        queue.add(Cell.createDummy());
        while (!queue.isEmpty()) {
          Cell cell = queue.remove();
          if (cell.isDummyCell) {
            currentDistance += 1;
            if (!queue.isEmpty()) {
              queue.add(Cell.createDummy());
            }
            continue;
          }
          if (grid[cell.x][cell.y] != 0) {
            continue;
          }
          grid[cell.x][cell.y] = currentDistance * -1;
          for (Cell c : getAdjacentNonBlockCells(cell, grid)) {
            queue.add(c);
          }
        }
        int destValue = grid[grid.length-1][grid[0].length-1];
        return destValue < 0 ? destValue * -1 : -1;
    }
    
    private static List<Cell> getAdjacentNonBlockCells(Cell cell, int[][] grid) {
        List<Cell> res = new LinkedList<>();
        List<Integer> shift = Arrays.asList(-1, 0, 1);
        int maxX = grid.length - 1;
        int maxY = grid[0].length - 1;
        for (int i : shift) {
          for (int j : shift) {
            int x = cell.x + i;
            int y = cell.y + j;
            if (x < 0 || x > maxX || y < 0 || y > maxY || grid[x][y] != 0) {
              continue;
            }
            res.add(Cell.createCell(x, y));
          }
        }
        return res;
    }
}
