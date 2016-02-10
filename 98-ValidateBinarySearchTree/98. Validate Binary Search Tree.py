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
        left,right = True,True
        if node.left !=None:
            if l_bound<node.left.val<node.val:
                left = self.helper(node.left,l_bound,node.val)
            else:
                return False
        if node.right !=None:
            if node.val<node.right.val< u_bound:
                right = self.helper(node.right,node.val,u_bound)
            else:
                return False
        return left and right


#Test case:
# # [1,1]
# # [3,1,5,0,2,4,6,null,null,null,3]
# # [-2147483648,null,2147483647]
