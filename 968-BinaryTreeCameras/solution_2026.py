# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # cache = {}

    # def helper(self, root: Optional[TreeNode], root_covered: bool, root_camera_optional: bool) -> int:
    #     if not root:
    #         return 0
    #     cache_key = (root, root_covered, root_camera_optional)
    #     if cache_key in self.cache:
    #         return self.cache[cache_key]
    #     root_w_camera = 1 + self.helper(root.left, True, True) + self.helper(root.right, True, True)
    #     left_w_camera = self.helper(root.left, False, False) + self.helper(root.right, False, True)
    #     right_w_camera = self.helper(root.left, False, True) + self.helper(root.right, False, False)
    #     both_optional = self.helper(root.left, False, True) + self.helper(root.right, False, True)
    #     candidates = [root_w_camera]
    #     if root_camera_optional:
    #         if root.left:
    #             candidates.append(left_w_camera)
    #         if root.right:
    #             candidates.append(right_w_camera)
    #         if root_covered:
    #             candidates.append(both_optional)
    #     min_camera = min(candidates)
    #     self.cache[cache_key] = min_camera
    #     return min_camera

    # def minCameraCover(self, root: Optional[TreeNode]) -> int:
    #     self.cache = {}
    #     return self.helper(root, False, True)

    def minSubtree(self, root: Optional[TreeNode]) -> Iterable[int]:
        """
        return 3 possible min under different restrictions: 
          - 1: have parent covered
          - 2: at least self-covered
          - 3: need cover from parent

          1 >= 2 >= 3
        """
        if not root: return (1001, 0, 0)
        left = self.minSubtree(root.left)
        right = self.minSubtree(root.right)

        case_1_min = 1 + left[2] + right[2]
        case_2_min = min(case_1_min, left[0] + right[1], left[1] + right[0])
        case_3_min = min(case_2_min, left[1] + right[1])
        return (case_1_min, case_2_min, case_3_min)

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return self.minSubtree(root)[1]
