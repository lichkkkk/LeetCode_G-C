__author__ = 'liuxiyun'
#Follow up for 21
# O(knlogk)
# 如果list数量不多但是每个list里元素特别特别多，要用什么办(heap比binary好) WHY???

# Heap
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return None
        h = []
        for node in lists:
            if node!=None:
                heapq.heappush(h,(node.val,node))
        fakenode = head = ListNode(0)
        while h:
            value,node = heapq.heappop(h)
            head.next = node
            head = head.next
            if node.next:
                heapq.heappush(h,(node.next.val,node.next))
        return fakenode.next

# Binary
from collections import deque
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []: # should write before lists = deque(lists)
            return None
        lists = deque(lists)
        while len(lists)>1:
            l1 = lists.popleft()
            l2 = lists.popleft()
            lists.append(self.merge(l1,l2))
        return lists[0]
    def merge(self,l1,l2):
        head = fakenode = ListNode(0)
        while l1!= None and l2!=None:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next
        if l1!=None:
            head.next = l1
        if l2!=None:
            head.next = l2
        return fakenode.next