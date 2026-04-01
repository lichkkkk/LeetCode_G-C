class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        res = set()
        for i, j, k in itertools.combinations(digits, 3):
            for a, b, c in itertools.permutations([i, j, k]):
                if a == 0 or c % 2: continue
                res.add(a * 100 + b * 10 + c)
        return len(res)
