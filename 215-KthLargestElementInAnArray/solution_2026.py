class Solution:
    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)  # heapq is a min heap
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        assert len(nums) >= k
        pivot = nums[0]
        left, mid, right = [], [], []
        for n in nums:
            if n < pivot: left.append(n)
            elif n == pivot: mid.append(n)
            else: right.append(n)
        if len(right) >= k: return self.findKthLargest(right, k)
        elif len(right) + len(mid) >= k: return pivot
        else: return self.findKthLargest(left, k - len(right) - len(mid)) 
