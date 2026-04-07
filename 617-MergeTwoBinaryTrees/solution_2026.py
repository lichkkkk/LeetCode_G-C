class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            rt = TreeNode()
            rt.val = root1.val + root2.val
            rt.left = self.mergeTrees(root1.left, root2.left)
            rt.right = self.mergeTrees(root1.right, root2.right)
            return rt
        elif root1:
            return root1
        else:
            return root2
