class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        occ = set(c.values())
        return len(c) == len(occ)
