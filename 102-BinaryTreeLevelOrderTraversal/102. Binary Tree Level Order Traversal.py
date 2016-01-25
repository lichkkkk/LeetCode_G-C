__author__ = 'liuxiyun'
# BFS:
# use queue
# Time: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root==None:
            return res
        queue = deque()
        queue.append((root,0))
        prelevel=-1
        while queue:
            node,level=queue.popleft()
            if level!= prelevel: # check if it's a new level
                prelevel = level
                res.append([])
            res[-1].append(node.val) # add node's val to the last list in result
            if node.left!=None:
                queue.append((node.left,level+1))
            if node.right!=None:
                queue.append((node.right,level+1))
        return res

# Test case:
# # []
# # [1]
# # [1,2,3,null,null,4]