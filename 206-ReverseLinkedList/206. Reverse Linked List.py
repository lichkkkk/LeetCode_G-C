__author__ = 'liuxiyun'
# iterative
# three Pointers
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return None
        sentinel = None
        node = head
        a = sentinel
        b = node
        while b != None:
           c = b.next #save the next node
           b.next = a
           a = b
           b = c
        return a
    
# recursive
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        return self.helper(node,None)
    def helper(self,node,pre):
        if node==None:
            return pre
        pos = node.next
        node.next = pre
        pre = node
        node = pos
        return self.helper(node,pre)