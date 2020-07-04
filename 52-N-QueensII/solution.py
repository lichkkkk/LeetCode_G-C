class Solution:
    def totalNQueens(self, n: int) -> int:
        return self.place(n, [])
        
    def place(self, n, placed):
        row = len(placed)
        if row == n:
            return 1
        res = 0
        for i in range(n):
            if any([i == placed[j] or abs(i - placed[j]) == row - j for j in range(row)]):
                continue
            placed.append(i)
            res += self.place(n, placed)
            placed.pop()
        return res
