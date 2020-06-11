# You can find a better solution here:
# https://leetcode.com/problems/linked-list-cycle-ii/discuss/44793/O(n)-solution-by-using-two-pointers-without-change-anything
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast == None or fast.next == None:
            return None
        # ok, we know it has cycle till here, and fast == slow
        cycle_length = 1
        fast = fast.next
        while fast != slow:
            fast = fast.next
            cycle_length += 1
        # we get the length of the cycle, let's find the pos
        fast = slow = head
        for _ in range(cycle_length):
            fast = fast.next
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
