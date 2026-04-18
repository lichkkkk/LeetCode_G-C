class Solution:

    def getSurrounding(self, image: List[List[int]], x: int, y: int) -> Iterator[tuple[int, int]]:
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            nx, ny = x + dx, y + dy
            if (not 0 <= nx < len(image)) or (not 0 <= ny < len(image[0])):
                continue
            yield nx, ny

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        curr_color = image[sr][sc]
        if curr_color == color:
            return image
        image[sr][sc] = color
        q.append((sr, sc))
        while q:
            x, y = q.popleft()
            for nx, ny in self.getSurrounding(image, x, y):
                if image[nx][ny] == curr_color:
                    image[nx][ny] = color
                    q.append((nx, ny))
        return image
