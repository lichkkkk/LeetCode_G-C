__author__ = 'liuxiyun'
# Idea:
# Just walk down from the whole tree's root as long as both p and q are in the same subtree
# (meaning their values are both smaller or both larger than root's).
# This walks straight from the root to the LCA, not looking at the rest of the tree, so it's pretty much as fast as it gets.
# O(1) space O(h) time

# Iterative
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        node=root
        while True:
            if (p.val <= node.val <= q.val) or (q.val <= node.val <= p.val):
                return node
            elif p.val < node.val and q.val < node.val:
                node = node.left
            else:
                node = node.right
# Recursive
def lowestCommonAncestor(self, root, p, q):
    if p.val < root.val > q.val:
        return self.lowestCommonAncestor(root.left, p, q)
    if p.val > root.val < q.val:
        return self.lowestCommonAncestor(root.right, p, q)
    return root
    
# Test case:
# Root
# p or q
# other