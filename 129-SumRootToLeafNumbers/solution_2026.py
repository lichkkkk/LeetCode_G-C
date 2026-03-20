# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: TreeNode, curr: int) -> int:
        if not root: return 0
        if not root.left and not root.right:
            return int(curr + str(root.val))
        res = 0
        res += self.helper(root.left, curr + str(root.val))
        res += self.helper(root.right, curr + str(root.val))
        return res

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, '')
