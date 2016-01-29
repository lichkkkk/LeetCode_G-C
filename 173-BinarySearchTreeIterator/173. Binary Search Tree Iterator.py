__author__ = 'liuxiyun'


# This problem is like a real-time inorder traversel

# I use Stack to store directed left children from root.
# When hasnext() be called, I just pop one element and this element is what next() should return
# In next(), I process its right child as new root, and put the left children into stack
# So this can satisfy O(h) memory, hasNext() in O(1) time,
# But next() is O(h) time.

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        node = root
        while node != None:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack == []:
            return False
        self.next_node = self.stack.pop()
        return True

    def next(self):
        """
        :rtype: int
        """
        self.add_node = self.next_node.right
        while self.add_node!=None:
            self.stack.append(self.add_node)
            self.add_node = self.add_node.left
        return self.next_node.val




# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())