class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        x2, x1 = head, head
        while x1 and x2:
            x1 = x1.next
            if not x1: return False
            x2 = x2.next
            if not x2: return False
            x2 = x2.next
            if x1 == x2: return True
        return False
