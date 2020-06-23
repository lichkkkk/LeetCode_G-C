# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        res = []
        dq = deque()
        dq.append(root)
        currLevelCnt = 1
        while currLevelCnt > 0:
            nextLevelCnt = 0
            currLevelNodes = []
            for _ in range(currLevelCnt):
                currNode = dq.popleft()
                currLevelNodes.append(currNode.val)
                if currNode.left != None:
                    dq.append(currNode.left)
                    nextLevelCnt += 1
                if currNode.right != None:
                    dq.append(currNode.right)
                    nextLevelCnt += 1
            res.append(currLevelNodes)
            currLevelCnt = nextLevelCnt
        return res
