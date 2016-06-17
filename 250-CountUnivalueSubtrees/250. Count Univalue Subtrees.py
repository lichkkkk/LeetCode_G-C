__author__ = 'liuxiyun'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.helper(root)
        return self.count
    def helper(self,node):
        if node == None:
            return True
        else:
            child_uni_left = self.helper(node.left)
            child_uni_right = self.helper(node.right)
        this_uni = True
        if node.left:
            if node.val != node.left.val:
                this_uni = False
        if node.right:
            if node.val!=node.right.val:
                this_uni = False
        uni = this_uni and child_uni_left and child_uni_right
        if uni:
            self.count+=1
        return uni