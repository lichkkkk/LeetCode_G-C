__author__ = 'liuxiyun'
# Backtracking
# Exponential time
class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        return self.helper(s)

    def helper(self,s):
        for i in range(len(s)-1):
            if s[i]==s[i+1]=="+":
                win = not self.helper(s[:i]+["-","-"]+s[i+2:])
                if win:
                    return True
        return False

# Use hashmap to remove duplicate
class Solution2(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = list(s)
        self.visited = {}
        return self.helper(s)

    def helper(self,s):
        if tuple(s) in self.visited:
            return self.visited[tuple(s)]
        for i in range(len(s)-1):
            if s[i]==s[i+1]=="+":
                win = not self.helper(s[:i]+["-","-"]+s[i+2:])
                self.visited[tuple(s[:i]+["-","-"]+s[i+2:])] = not win
                if win:
                    return True
        return False