# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEqualTree(self, root1, root2) -> bool:
        if not root1 and not root2: return True
        if not root1 or not root2: return False
        return (root1.val == root2.val
                and self.isEqualTree(root1.left, root2.left)
                and self.isEqualTree(root1.right, root2.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        if self.isEqualTree(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
