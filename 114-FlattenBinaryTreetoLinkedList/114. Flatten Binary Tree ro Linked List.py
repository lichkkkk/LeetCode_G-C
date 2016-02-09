__author__ = 'liuxiyun'

# Time: O(n). Every node is visited by 'add' only once

class Solution(object):
    def zijixiede(self,root):
        if root == None:
                return
        node = root
        while node:
            if node.left:
                right = node.right
                add = node.left
                while  add.right:
                    add = add.right
                add.right = right
                node.right = node.left
                node.left = None #!!!
            node = node.right

#[1,nul,2,3]