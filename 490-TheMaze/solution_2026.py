class Solution:
    def findNext(self, maze, start) -> List[Tuple[int]]:
        x, y = start
        max_x, max_y = len(maze), len(maze[0])
        res = []
        for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            nx, ny = x, y
            while 0 <= nx < max_x and 0 <= ny < max_y and maze[nx][ny] == 0:
                nx, ny = nx + dx, ny + dy
            nx, ny = nx - dx, ny - dy
            if (nx, ny) != (x, y):
                res.append((nx, ny))
        return res

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        start, dest = tuple(start), tuple(destination)
        visited = set()
        visited.add(start)
        queue = deque([start])
        while queue:
            curr_start = queue.popleft()
            for next_start in self.findNext(maze, curr_start):
                if next_start == dest: return True
                if next_start in visited: continue
                visited.add(next_start)
                queue.append(next_start)
        return False
