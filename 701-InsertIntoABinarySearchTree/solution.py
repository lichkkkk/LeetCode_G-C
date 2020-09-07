# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val)
        else:
            self.insertHelper(root, val)
            return root
        
    def insertHelper(self, root, val):
        if val == root.val:
            return
        elif val < root.val:
            if root.left == None:
                root.left = TreeNode(val)
            else:
                self.insertHelper(root.left, val)
        else:
            if root.right == None:
                root.right = TreeNode(val)
            else:
                self.insertHelper(root.right, val)
