"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        if root.children == None:
            return 1
        max_children_depth = 0
        for child in root.children:
            max_children_depth = max(max_children_depth, self.maxDepth(child))
        return max_children_depth + 1
        
