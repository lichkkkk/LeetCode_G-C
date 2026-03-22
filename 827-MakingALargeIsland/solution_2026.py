class Solution:
    def get_adjacent_pos(
        self, grid: List[List[int]], x: int, y: int
    ) -> List[Tuple[int, int]]:
        res = []
        for x_d, y_d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + x_d, y + y_d
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                res.append((nx, ny))
        return res

    # Always be careful of using recussion -> it may blow up the stack if the input is large
    # Python default recurssion limit is 1000
    def color_island_recurssion(
        self, grid: List[List[int]], i: int, x: int, y: int
    ) -> int:
        """
        color an island from pos (x, y), flip all 1 in the island to be i, return the size
        """
        if grid[x][y] != 1:
            return 0
        grid[x][y] = i
        size = 1
        for nx, ny in self.get_adjacent_pos(grid, x, y):
            size += self.color_island(grid, i, nx, ny)
        return size

    def color_island(self, grid: List[List[int]], i: int, x: int, y: int) -> int:
        """
        color an island from pos (x, y), flip all 1 in the island to be i, return the size
        """
        stack = [(x, y)]
        size = 0
        while stack:
            x, y = stack.pop()
            if grid[x][y] != 1:
                continue
            grid[x][y] = i
            size += 1
            for nx, ny in self.get_adjacent_pos(grid, x, y):
                stack.append((nx, ny))
        return size

    def find_all_adjacent_islands(
        self, grid: List[List[int]], x: int, y: int
    ) -> Set[int]:
        """
        given a pos (x, y), return all islands connected to this pos (up to 4)
        """
        res = set()
        for nx, ny in self.get_adjacent_pos(grid, x, y):
            i = grid[nx][ny]
            if i > 1:
                res.add(i)
        return res

    def largestIsland(self, grid: List[List[int]]) -> int:
        # Step 1: color all existing islands
        curr_index = 2
        size_by_index = {}
        curr_largest = 0
        len_x, len_y = len(grid), len(grid[0])
        for x in range(len_x):
            for y in range(len_y):
                if grid[x][y] != 1:
                    continue
                curr_size = self.color_island(grid, curr_index, x, y)
                size_by_index[curr_index] = curr_size
                curr_largest = max(curr_largest, curr_size)
                curr_index += 1

        # Step 2: iterate through all 0 and find the optimal flip
        for x in range(len_x):
            for y in range(len_y):
                if grid[x][y] != 0:
                    continue
                connected_islands = self.find_all_adjacent_islands(grid, x, y)
                curr_size = sum(size_by_index[i] for i in connected_islands) + 1
                curr_largest = max(curr_largest, curr_size)

        # debug
        # for r in grid: print(r)
        return curr_largest
