class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_1 = ListNode(-101, list1)
        dummy_2 = ListNode(-102, list2)
        res = ListNode(0, None)
        res_tail = res
        while dummy_1.next and dummy_2.next:
            if dummy_1.next.val > dummy_2.next.val:
                res_tail.next = dummy_2.next
                dummy_2.next = dummy_2.next.next
                res_tail = res_tail.next
                res_tail.next = None
            else:
                res_tail.next = dummy_1.next
                dummy_1.next = dummy_1.next.next
                res_tail = res_tail.next
                res_tail.next = None
        if dummy_1.next:
            res_tail.next = dummy_1.next
        elif dummy_2.next:
            res_tail.next = dummy_2.next
        return res.next
