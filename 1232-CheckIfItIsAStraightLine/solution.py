class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) < 2:
            return True
        p1 = [coordinates[1][0]-coordinates[0][0], coordinates[1][1]-coordinates[0][1]]
        for i in xrange(2, len(coordinates)):
            pi = [coordinates[i][0]-coordinates[0][0], coordinates[i][1]-coordinates[0][1]]
            if p1[0]*pi[1] != p1[1]*pi[0]:
                return False
        return True
