# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None
        mid = len(nums) // 2
        return TreeNode(
            val=nums[mid],
            left=self.sortedListToBST(nums[:mid]),
            right=self.sortedListToBST(nums[mid+1:])
        )

    def bstToSortedList(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: return res
        stack = []
        while root:
            stack.append(root)
            root = root.left
        while stack:
            n = stack.pop()
            res.append(n.val)
            n = n.right
            while n:
                stack.append(n)
                n = n.left
        return res

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.sortedListToBST(self.bstToSortedList(root))
