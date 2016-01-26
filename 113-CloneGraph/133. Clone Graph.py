__author__ = 'liuxiyun'
# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


# DFS (explore every new node we meet for now)
#
# In order to clone a graph, you need to have a copy of each node in the original graph.
# https://leetcode.com/discuss/41944/7-17-lines-c-bfs-dfs-solutions

# Use a dictionary to store the UndirectedGraphNode which have been created
# Iterative:
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if node == None:
            return None
        stack = [node]
        dic = {}
        root = UndirectedGraphNode(node.label)
        dic[node.label] = root # create a dictionary. key is label, value is new clone node

        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor.label not in dic: # if it is a new node for our clone graph
                    stack.append(neighbor) # put it into stack so that we can explore it later
                    dic[neighbor.label] = UndirectedGraphNode(neighbor.label) # creat the new node and put it into dictionary
                dic[node.label].neighbors.append(dic[neighbor.label]) # add the neighbor to the node in clone graph
        return root

# Recursive
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if node == None:
            return None
        stack = [node]
        self.dic = {}
        root = UndirectedGraphNode(node.label)
        self.dic[node.label] = root # create a dictionary. key is label, value is new clone node
        self.explore(node)
        return root
    def explore(self,node):
        for neighbor in node.neighbors:
            if neighbor.label not in self.dic: # if it is a new node for our clone graph
                #stack.append(neighbor) # put it into stack so that we can explore it later
                self.dic[neighbor.label] = UndirectedGraphNode(neighbor.label) # creat the new node and put it into dictionary
                self.explore(neighbor)
            self.dic[node.label].neighbors.append(self.dic[neighbor.label]) # add the neighbor to the node in clone graph
        return

# Test case:
# {0,1,2#1,2#2,2}
# {0,0,0}