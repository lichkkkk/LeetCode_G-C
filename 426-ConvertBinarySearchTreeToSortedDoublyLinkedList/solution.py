"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        ll = self.treeToDoublyList(root.left)
        rl = self.treeToDoublyList(root.right)
        root.left = root.right = root
        return self._append(ll, self._append(root, rl))
        
    def _append(self, ll, rl):
        if not ll:
            return rl
        if not rl:
            return ll
        ll_start, ll_end = ll, ll.left
        rl_start, rl_end = rl, rl.left
        ll_end.right = rl_start
        rl_start.left = ll_end
        ll_start.left = rl_end
        rl_end.right = ll_start
        return ll_start
