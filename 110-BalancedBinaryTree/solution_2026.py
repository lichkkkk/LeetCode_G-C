# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root) -> int:
        if not root: return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        if abs(l - r) > 1: return -1
        if l < 0 or r < 0: return -1
        return max(l, r) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root) >= 0
