__author__ = 'liuxiyun'

# # Idea: Based on the defination of binary search tree:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# We do a recursive way.
# There are two situations that we need to return False. if the left child is not in the correct value range or the right child...
# What is the right range? for a left child of node, the upperbound should be the node.val, for a right child, the lower bound should be the node.val
# However, for a left child of node, it should also have a lowerbound, which is inherent from the node. same as right child

# Edge case: -2147483648,2147483647 is a correct input. Therefore the raw lower bound and upper bound should be -2147483649,2147483648

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.helper(root,-2147483649,2147483648)
    def helper(self,root,l_bound,u_bound,left_child):
        if root == None:
            return True
        if root.left !=None and  (root.left.val<=l_bound or root.left.val >= root.val):
            return False
        if root.right !=None and  (root.right.val<=root.val or root.right.val >= u_bound):
            return False
        return self.helper(root.left,l_bound,root.val) and self.helper(root.right,root.val,u_bound)


#Test case:
# # [1,1]
# # [3,1,5,0,2,4,6,null,null,null,3]
# # [-2147483648,null,2147483647]