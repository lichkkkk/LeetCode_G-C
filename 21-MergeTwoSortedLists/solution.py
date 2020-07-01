# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
      dummy = ListNode()
      head = dummy
      while l1 and l2:
        if l1.val > l2.val:
          head.next = l2
          l2 = l2.next
        else:
          head.next = l1
          l1 = l1.next
        head = head.next
      if l1:
        head.next = l1
      else:
        head.next = l2
      return dummy.next
