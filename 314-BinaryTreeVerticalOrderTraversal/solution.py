# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
The time complexity is O(NlogN) because of the sort in the end. However there is a smart way to
get rid of the sort: bookkeep the max/min offset when doing the BFS. Such that you can avoid the 
sort by going through the dict in order.

It's easy to understand why a sort is not necessary intuitively. Should think more while noticing
things like this.

It is difficult to solve this problem with DFS, because DFS does not guarantee any strict order 
(either top -> down or left -> right. But for BFS, it's strictly top-down + left-right. It's just 
in this question it asks for left-right first then top-down)
"""

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = defaultdict(list)
        queue = deque()
        queue.append((root, 0))
        while len(queue) > 0:
            level_size = len(queue)
            for i in range(level_size):
                node, offset = queue.popleft()
                res[offset].append(node.val)
                if node.left:
                    queue.append((node.left, offset - 1))
                if node.right:
                    queue.append((node.right, offset + 1))
        return [v for k, v in sorted(res.items())]
