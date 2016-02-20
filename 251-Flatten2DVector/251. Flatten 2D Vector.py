__author__ = 'liuxiyun'
# Use row and col points to the ele need to add next
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.row = 0
        self.vec2d = vec2d
        # if empty, go to next row. Be careful about [[]] or []
        while self.row < len(self.vec2d) and self.vec2d[self.row]==[]:
            self.row+=1
        self.col = 0
        self.new_list = []

    def next(self):
        """
        :rtype: int
        """
        i = self.col
        j = self.row
        self.col +=1
        if self.col == len(self.vec2d[self.row]): # move to next ele
            self.col=0
            self.row+=1
            while self.row<len(self.vec2d) and self.vec2d[self.row] == []: # if empty, go to next row
                self.row+=1
        return self.vec2d[j][i]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.row == len(self.vec2d):
            return False
        return True

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())