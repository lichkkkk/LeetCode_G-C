# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        _, res = self.helper(root, k)
        return res
        
    def helper(self, root, k):
        if not root:
            return (0, None)
        left_cnt, res = self.helper(root.left, k)
        if res != None:
            return (-1, res)
        elif left_cnt == k - 1:
            return (-1, root.val)
        else:
            right_cnt, res = self.helper(root.right, k - left_cnt - 1)
            return (left_cnt + right_cnt + 1, res)
