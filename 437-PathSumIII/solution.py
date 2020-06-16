# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        return self.helper(root, targetSum, [])
        
    def helper(self, root, targetSum, currSumList):
        if root == None:
            return 0
        res = 0
        for i in range(len(currSumList)):
            currSumList[i] += root.val
            if currSumList[i] == targetSum:
                res += 1
        if root.val == targetSum:
            res += 1
        currSumList.append(root.val)
        res += self.helper(root.left, targetSum, currSumList)
        res += self.helper(root.right, targetSum, currSumList)
        currSumList.pop()
        for i in range(len(currSumList)):
            currSumList[i] -= root.val
        return res
    
# This solution can be further improved by a cache
