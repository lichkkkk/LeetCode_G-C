# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, root.val)

    def helper(self, root, currMax):
        if root == None:
            return 0
        res = 1 if root.val >= currMax else 0
        currMax = max(currMax, root.val)
        res += self.helper(root.left, currMax) + self.helper(root.right, currMax)
        return res
