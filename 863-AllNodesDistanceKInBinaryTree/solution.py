# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if K == 0:
            return [target.val]
        nodes = []
        self._find(root, target, nodes)
        res = []
        for i in range(len(nodes)):
            #print(nodes[i].val)
            if K - i == 0:
                res.append(nodes[i].val)
                break
            if i == 0:
                self._find_distance(nodes[i].left, K-i-1, res)
                self._find_distance(nodes[i].right, K-i-1, res)
            else:
                if nodes[i].left == nodes[i-1]:
                    self._find_distance(nodes[i].right, K-i-1, res)
                else:
                    self._find_distance(nodes[i].left, K-i-1, res)
        return res
            
    def _find(self, root, target, path):
        if not root:
            return False
        if root == target or self._find(root.left, target, path) or self._find(root.right, target, path):
            path.append(root)
            return True
        else:
            return False
        
    def _find_distance(self, root, distance, res):
        if not root:
            return
        #print(root.val, distance, res)
        if not distance:
            res.append(root.val)
        else:
            self._find_distance(root.left, distance-1, res)
            self._find_distance(root.right, distance-1, res)
