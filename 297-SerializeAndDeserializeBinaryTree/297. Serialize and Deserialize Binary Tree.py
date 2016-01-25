__author__ = 'liuxiyun'
# Idea:
# preorder traverse to save the value of node, and use '#' to mark the None node
# #

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        self.vals = []
        self.help_s(root) #['1','2','#','#','3','4'.....]
        return ' '.join(self.vals) # "1 2 # # 3 4 # # 5 # #"

    def help_s(self,node):
        if node:
            self.vals.append(str(node.val))
            self.help_s(node.left)
            self.help_s(node.right)
        else:
            self.vals.append('#')

    def deserialize(self, data):
        self.vals2 = iter(data.split()) # iter: built-in function. call next() to get the next element
        return self.help_d()

    def help_d(self):
        val = next(self.vals2)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = self.help_d()
        node.right = self.help_d()
        return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Test case:
# # []
# # only has left children
# # only has right children
# # no children