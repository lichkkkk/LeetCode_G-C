# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None:
            return None
        if root.val == key:
            if root.left:
                if root.left.right == None:
                    root.left.right = root.right
                    root = root.left
                else:
                    largest_s_parent = root.left
                    while largest_s_parent.right.right:
                        largest_s_parent = largest_s_parent.right
                    root.val = largest_s_parent.right.val
                    largest_s_parent.right = largest_s_parent.right.left
            elif root.right:
                if root.right.left == None:
                    root.right.left = root.left
                    root = root.right
                else:
                    smallest_s_parent = root.right
                    while smallest_s_parent.left.left:
                        smallest_s_parent = smallest_s_parent.left
                    root.val = smallest_s_parent.left.val
                    smallest_s_parent.left = smallest_s_parent.left.right
            else:
                return None
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
