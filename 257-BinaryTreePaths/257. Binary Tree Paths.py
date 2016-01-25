__author__ = 'liuxiyun'

# Backtracking or DFS
# Time: O(n) = # of path = n/2
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.res = []
        if root==None:
            return []
        temp =''
        node=root
        self.dfs(temp,node)
        return self.res
    def dfs(self,temp,node):
        if node.left==None and node.right==None:
            self.res.append(temp+str(node.val))
            return
        if node.left!=None:
            self.dfs(temp+str(node.val)+'->',node.left)
        if node.right!=None:
            self.dfs(temp+str(node.val)+'->',node.right)

# Test case
# # []
# # [1,2,3]
# # [1,2,3,#,#,4,#]

