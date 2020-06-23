# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.helper(res, 0, root)
        return res
    
    def helper(self, res, level, root):
        if root == None:
            return
        if level > len(res) + 1:
            print("error")
            return
        if level == len(res):
            res.append([])
        if level % 2 == 0:
            res[level].append(root.val)
        else:
            res[level].insert(0, root.val)
        self.helper(res, level + 1, root.left)
        self.helper(res, level + 1, root.right)
