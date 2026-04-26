class Solution:
    def get_good_oranges_around(self, grid, x, y) -> Iterable[tuple[int, int]]:
        for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            nx, ny = x + dx, y + dy
            if not 0 <= nx < len(grid):
                continue
            if not 0 <= ny < len(grid[0]):
                continue
            if grid[nx][ny] == 1:
                yield (nx, ny)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        init_bad_oranges = []
        left_good_oranges_cnt = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    init_bad_oranges.append((x, y))
                elif grid[x][y] == 1:
                    left_good_oranges_cnt += 1
        steps = 0
        next_bad_oranges = set()
        for x, y in init_bad_oranges:
            for nx, ny in self.get_good_oranges_around(grid, x, y):
                next_bad_oranges.add((nx, ny))
        while next_bad_oranges:
            next_next_bad_oranges = set()
            for x, y in next_bad_oranges:
                grid[x][y] = 2
                left_good_oranges_cnt -= 1
                for nx, ny in self.get_good_oranges_around(grid, x, y):
                    next_next_bad_oranges.add((nx, ny))
            ## dedup is important in BFS
            next_bad_oranges = next_next_bad_oranges - next_bad_oranges
            steps += 1
        if not left_good_oranges_cnt:
            return steps
        else:
            return -1
 
