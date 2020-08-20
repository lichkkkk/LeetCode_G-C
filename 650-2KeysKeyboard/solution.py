class Solution:
    def minSteps(self, n: int) -> int:
        table = list(range(n+1))
        table[1] = 0
        for i in range(2, n+1):
            for div in range(1, i):
                if div * 2 > i:
                    break
                if i % div != 0:
                    continue
                table[i] = min(table[i], i//div + table[div])
        return table[-1]
