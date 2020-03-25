# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
      return self.sumOfLeftLeavesHelper(root, False)
    
    def sumOfLeftLeavesHelper(self, root: TreeNode, is_left: bool) -> int:
      if root == None:
        return 0
      if root.left == None and root.right == None and is_left:
        return root.val
      return self.sumOfLeftLeavesHelper(root.left, True) + \
             self.sumOfLeftLeavesHelper(root.right, False)
