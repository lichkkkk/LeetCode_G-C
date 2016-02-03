class Solution(object):
    def isValidBST(self, root):
        bound = 1<<33 
        return self.helper(root, -bound, bound)
    def helper(self,root,l_bound,u_bound):
        if root == None:
            return True
        if not l_bound < root.val < u_bound: 
            return False
        return self.helper(root.left, l_bound, root.val) and\
               self.helper(root.right,root.val,u_bound)
