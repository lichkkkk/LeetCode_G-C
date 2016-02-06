__author__ = 'liuxiyun'
# dfs

from collections import defaultdict
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        self.visit = [False] * n
        self.dic = defaultdict(list)
        for i,j in edges:
            self.dic[i].append(j)
            self.dic[j].append(i)
        cc = 0
        for node in range(0,n):
            if self.visit[node] == False:
                self.visit[node]=True
                self.explore(node)
                cc+=1
        return cc
    def explore(self,node):
        for neighbor in self.dic[node]:
            if self.visit[neighbor]==False:
                self.visit[neighbor] = True
                self.explore(neighbor)