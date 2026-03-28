class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        prev = -1 * duration
        for t in timeSeries:
            total += duration - max(prev + duration - t, 0)
            prev = t
        return total
