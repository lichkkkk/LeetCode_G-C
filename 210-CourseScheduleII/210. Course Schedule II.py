__author__ = 'liuxiyun'
# Topological order
# O(n)
# Be careful about infinit loop list [1,2],[2,1]
from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        n = numCourses
        self.visit = [False]*n
        self.dic = defaultdict(list)
        self.res = []
        for cur,pre in prerequisites:
            self.dic[cur].append(pre)
        for i in range(n):
            if not self.visit[i]:
                self.temp_vi = [False]*n
                self.temp_vi[i] = True
                if not self.help(i):
                    return []
        return self.res
    def help(self,i):
        print i
        self.visit[i] = True
        if i in self.dic:
            for pre in self.dic[i]:
                if self.temp_vi[pre]:
                    return False
                elif self.visit[pre]==False:
                    self.temp_vi[pre] = True # set
                    if not self.help(pre):
                        return False
                    self.temp_vi[pre] = False # reset
        self.res.append(i)
        return True
c=Solution()
print c.findOrder(3,[[0,1],[0,2],[1,2]])