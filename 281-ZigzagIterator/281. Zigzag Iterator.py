__author__ = 'liuxiyun'

# linkedlist + queue
# O(m+n)
class Linkedlist_node(object):
    def __init__(self,val):
        self.val = val
        self.next = None
from collections import deque
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        pre1,pre2 = Linkedlist_node(0),Linkedlist_node(0)
        head1,head2 = pre1,pre2 # ALWAYS FORGET
        for num in v1:
            node = Linkedlist_node(num)
            pre1.next = node
            pre1 = pre1.next
        for num in v2:
            node = Linkedlist_node(num)
            pre2.next = node
            pre2 = pre2.next
        self.d = deque()
        if head1.next: # CHECK []
            self.d.append(head1.next)
        if head2.next:
            self.d.append(head2.next)


    def next(self):
        """
        :rtype: int
        """
        node = self.d.popleft()
        if node.next:
            self.d.append(node.next)
        return node.val

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.d else False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

# 2
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 ,self.v2= v1,v2
        self.point = 0
        self.i = 0
        self.j = 0
        self.length = len(v1) + len(v2) -1
        self.stop = min(len(v1),len(v2))*2-1

    def next(self):
        """
        :rtype: int
        """
        if self.point <= self.stop:
            if self.point %2 ==0:
                add = self.v1[self.i]
                self.i+=1
            else:
                add = self.v2[self.j]
                self.j+=1
        else:
            if self.i == len(self.v1):# add j
                add = self.v2[self.j]
                self.j+=1
            else:
                add = self.v1[self.i]
                self.i+=1
        self.point +=1
        return add


    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.point <=self.length else False


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())