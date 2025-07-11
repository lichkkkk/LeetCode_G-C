class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = list(range(1, n+1))
        pos = 0
        while len(l) > 1:
            pos = (pos + k - 1) % len(l)
            del l[pos]
            pos = pos % len(l)
        return l[0]
