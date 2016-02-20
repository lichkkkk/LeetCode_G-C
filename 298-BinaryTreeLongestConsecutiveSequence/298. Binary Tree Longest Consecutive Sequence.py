__author__ = 'liuxiyun'
# Bottom up
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_len = 0
        self.helper(root)
        return self.max_len
    def helper(self,node):
        if node == None:
            return [0,0]
        left = self.helper(node.left)
        right = self.helper(node.right)
        if node.left == None or node.val!=node.left.val-1:
            left = 1
        else:
            left+=1
        if node.right == None or node.val!=node.right.val-1:
            right = 1
        else:
            right+=1
        self.max_len = max(left,right,self.max_len)
        return max(left,right)
# Top down
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_len = 0
        if root == None:
            return 0
        self.helper(root,0,root.val)
        return self.max_len
    def helper(self,node,cur,target):
        if node == None:
            return
        if node.val == target:
            cur+=1
        else:
            cur = 1
        self.max_len= max(self.max_len,cur)
        self.helper(node.left,cur,node.val+1)
        self.helper(node.right,cur,node.val+1)