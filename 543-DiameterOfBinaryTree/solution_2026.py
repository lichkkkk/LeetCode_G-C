# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def _process_sub_tree(self, root: Optional[TreeNode]) -> tuple[int, int]:
        '''take a root, return (longest_path, diameter in #nodes)

        It's easier to use # of nodes compared to edges 
        '''
        if not root: return 0, 0
        left_longest, left_d = self._process_sub_tree(root.left)
        right_longest, right_d = self._process_sub_tree(root.right)
        d = max([left_d, right_d, left_longest+right_longest+1])
        longest = max(left_longest+1, right_longest+1)
        return longest, d
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, res = self._process_sub_tree(root)
        return res - 1
