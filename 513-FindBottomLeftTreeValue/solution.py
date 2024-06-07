# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def helper(self, root: Optional[TreeNode]) -> (int, int):
      if not root:
        return 0, None
      depth_l, val_l = self.helper(root.left)
      depth_r, val_r = self.helper(root.right)
      if depth_l == 0 and depth_r == 0:
        return 1, root.val
      elif depth_r > depth_l:
        return depth_r + 1, val_r
      else:
        return depth_l + 1, val_l

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
      return self.helper(root)[1]
