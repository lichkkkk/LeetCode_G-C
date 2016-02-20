__author__ = 'liuxiyun'
# Based on observation, every node should have two child, whether the children is # or number
# need - there should be "need"number of signs(number or #) in this level
# n - there are "n"number of number in this level. it means, next level, "need" is 2*n
# if there are not enough signs in this level, return false
# if the elememts in the last level are not all #, return false
# else: return True

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if preorder=='':
            return True
        preorder = preorder.split(",")
        need = 1
        i=0
        while i< len(preorder):
            if i+need>len(preorder) or need == 0:
                return False
            n=0
            for j in range(need):
                if preorder[i+j]!='#':
                    n+=1
            i+=(need)
            need = 2*n

        return True if need == 0 else False