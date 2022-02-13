"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_path, q_path = set(), set()
        p_path.add(p.val)
        q_path.add(q.val)
        while p.val not in q_path and q.val not in p_path:
            if p.parent:
                p = p.parent
                p_path.add(p.val)
            if q.parent:
                q = q.parent
                q_path.add(q.val)
        return p if p.val in q_path else q
