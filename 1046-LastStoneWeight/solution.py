class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [s * -1 for s in stones]
        heapq.heapify(pq)
        while len(pq) > 1:
            one, two = heapq.heappop(pq), heapq.heappop(pq)
            if one != two:
                heapq.heappush(pq, one - two)
        return -1 * pq[0] if len(pq) else 0
