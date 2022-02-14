class Solution:

    def __init__(self, w: List[int]):
        self._w = [w[0]]
        for n in w[1:]:
            self._w.append(self._w[-1] + n)

    def pickIndex(self) -> int:
        val = random.randint(1, self._w[-1])
        return bisect.bisect_left(self._w, val)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
