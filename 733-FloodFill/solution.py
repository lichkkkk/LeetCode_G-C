class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.helper(image, sr, sc, image[sr][sc], newColor)
        return image
    
    def helper(self, image, sr, sc, oldColor, newColor):
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return
        if image[sr][sc] != oldColor or oldColor == newColor:
            return
        image[sr][sc] = newColor
        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for dr, dc in moves:
            self.helper(image, sr+dr, sc+dc, oldColor, newColor)
