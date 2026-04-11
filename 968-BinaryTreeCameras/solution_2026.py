# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cache = {}

    def helper(self, root: Optional[TreeNode], root_covered: bool, root_camera_optional: bool) -> int:
        if not root:
            return 0
        cache_key = (root, root_covered, root_camera_optional)
        if cache_key in self.cache:
            return self.cache[cache_key]
        root_w_camera = 1 + self.helper(root.left, True, True) + self.helper(root.right, True, True)
        left_w_camera = self.helper(root.left, False, False) + self.helper(root.right, False, True)
        right_w_camera = self.helper(root.left, False, True) + self.helper(root.right, False, False)
        both_optional = self.helper(root.left, False, True) + self.helper(root.right, False, True)
        candidates = [root_w_camera]
        if root_camera_optional:
            if root.left:
                candidates.append(left_w_camera)
            if root.right:
                candidates.append(right_w_camera)
            if root_covered:
                candidates.append(both_optional)
        min_camera = min(candidates)
        self.cache[cache_key] = min_camera
        return min_camera

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cache = {}
        return self.helper(root, False, True)
