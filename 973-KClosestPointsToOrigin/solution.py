# Two other interesting solutions: Distance-based Binary Search & Quick Select
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(p[0]**2+p[1]**2, i) for i, p in enumerate(points)]
        heapq.heapify(heap)
        return [points[heapq.heappop(heap)[1]] for _ in range(k)]
