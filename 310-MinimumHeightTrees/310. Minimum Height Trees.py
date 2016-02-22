__author__ = 'liuxiyun'
# Remove sink iteratively and one or two nodes that left is the answer.
# Time and Space: O(n)
from collections import defaultdict
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        self.dic = defaultdict(list)
        degree = [n]*n
        for pre,next in edges:
            self.dic[pre].append(next)
            self.dic[next].append(pre)
        sink = []
        for root in self.dic:
            degree[root] = len(self.dic[root])
            if degree[root]==1:
                sink.append(root)
        while n>2:
            n-=len(sink)
            new_sink=[]
            for node in sink:
                for x in self.dic[node]:
                    degree[x]-=1
                    if degree[x]==1:
                        new_sink.append(x)
            sink = new_sink
        return sink

# Check each node's height
# O(n^2)
from collections import defaultdict
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.dic = defaultdict(list)
        min_height = n
        self.height = [n]*n
        for pre,next in edges:
            self.dic[pre].append(next)
            self.dic[next].append(pre)
        for root in self.dic:
            self.visited = [False]*n
            self.height[root] = self.explore(root)
        min_height = min(self.height)
        res = []
        for node in range(len(self.height)):
            if self.height[node]==min_height:
                res.append(node)
        return res
    def explore(self,root):
        if root not in self.dic or self.visited[root]:
            return 0
        self.visited[root]=True
        return max(self.explore(x)+1 for x in self.dic[root])

