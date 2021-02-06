# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return max(self.helper(root)[0] - 1, 0)
    
    def helper(self, root):
        """
        return: (max diameter, longest branch)
        """
        if root == None:
            return 0, 0
        lmd, llb = self.helper(root.left)
        rmd, rlb = self.helper(root.right)
        md = max(lmd, rmd, llb + rlb + 1)
        lb = max(llb, rlb) + 1
        return md, lb
