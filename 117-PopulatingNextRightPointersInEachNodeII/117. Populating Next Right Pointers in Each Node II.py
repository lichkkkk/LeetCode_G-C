__author__ = 'liuxiyun'

# The algorithm is a BFS or level order traversal.
# We go through the tree level by level, each level, right to left
# Record the previous node and previous level.
# O(n) time, O(n) space


# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        queue = []
        if root == None:
            return
        pre_level = -1
        queue.append((root,0))
        while queue:
            node,level = queue.pop(0)
            if level != pre_level:
                node.next=None
            else:
                node.next = pre_node
            pre_level = level
            pre_node = node
            if node.right !=None:
                queue.append((node.right,level+1))
            if node.left != None:
                queue.append((node.left,level+1))


# The algorithm is a BFS or level order traversal.
#  We go through the tree level by level.
# node is the pointer in the parent level, tail is the tail pointer in the child level.
#  The parent level can be view as a singly linked list or queue, which we can traversal easily with a pointer.
# Connect the tail with every one of the possible nodes in child level, update it only if the connected node is not nil. Do this one level by one level. The whole thing is quite straightforward.
# O(1) space

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        node = root
        while node:
            tail = next_start = TreeLinkNode(0)
            while node:
                tail.next = node.left
                if node.left != None:
                    tail = tail.next
                tail.next = node.right
                if node. right!=None:
                    tail = tail.next
                node = node.next
            node = next_start.next