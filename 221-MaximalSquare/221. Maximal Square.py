__author__ = 'liuxiyun'

# DP
# https://leetcode.com/discuss/38489/easy-solution-with-detailed-explanations-8ms-time-and-space
# P[i][j] = min(P[i - 1][j], P[i][j - 1], P[i - 1][j - 1]) + 1
# Time: O(mn)
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == []:
            return 0
        size = [[0 for j in range(len(matrix[0]))]for i in range(len(matrix))]
        check1 = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='1':
                    size[i][j] = 1
                    check1 = True
        if check1 == False:
            return 0

        maxSquare = 1
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == '0':
                    # print "continue"
                    continue
                size[i][j] = min(size[i - 1][j - 1], min(size[i - 1][j], size[i][j - 1])) + 1
                maxSquare = max(size[i][j], maxSquare)
        return maxSquare**2
# Test case:
# #
# c=Solution()
# print c.maximalSquare([])
# print c.maximalSquare(['1'])
# print c.maximalSquare(['0'])
# print c.maximalSquare(['10','10'])
# print c.maximalSquare(['11','00'])
# print c.maximalSquare(['10100','10111','11111','10010'])
# print c.maximalSquare(["1111","1111","1111"])
# print c.maximalSquare(["1101","1101","1111"])
# print c.maximalSquare(["0001","1101","1111","0111","0111"])
# print c.maximalSquare(["000","000","111"])
