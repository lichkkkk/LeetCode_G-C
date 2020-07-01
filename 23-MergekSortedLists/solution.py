# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution(object):
    def mergeKLists2(self, lists):
        dummy = ListNode(None)
        curr = dummy
        pq = []
        counter = 0
        for node in lists:
            if node:
                heapq.heappush(pq, (node.val, counter, node))
                counter += 1
        while len(pq) > 0:
            curr.next = heapq.heappop(pq)[2]
            curr = curr.next
            if curr.next:
                heapq.heappush(pq, (curr.next.val, counter, curr.next))
                counter += 1
        return dummy.next
      
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        counter = 0
        for node in lists:
            if node:
                q.put((node.val, counter,node))
                counter += 1
        while q.qsize() > 0:
            curr.next = q.get()[2]
            curr = curr.next
            if curr.next:
                q.put((curr.next.val, counter, curr.next))
                counter += 1
        return dummy.next
      
"""
Complexity for this approach is O(klogk*n). We can also repeat -merge-2-lists for k, then
the complexity is O(k^2*n).
"""
