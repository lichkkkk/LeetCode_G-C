__author__ = 'liuxiyun'
# Put each node from preorder into stack
# If ## in stack, If the previous node is None or #, return False
# otherwise, remove them and replace the previous node with #
# if all the nodes have been added once to stack, and stack only has # in it, return True
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(",")
        stack = []
        i=0
        for i in range(len(preorder)):
            node = preorder[i]
            stack.append(node)
            if node == "#":
                while len(stack)>1 and stack[-1] == '#' and stack[-2]=="#":
                    stack.pop()
                    stack.pop()
                    if stack == [] or stack[-1]=='#':
                        return False
                    else:
                        stack[-1]="#"
        return True if stack == ['#'] else False
