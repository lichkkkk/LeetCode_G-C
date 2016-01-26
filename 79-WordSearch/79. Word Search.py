__author__ = 'liuxiyun'

# Go through every element, do dfs.
# don't forget to track if the element is already visited when dfs

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[str]
        :type word: str
        :rtype: bool
        """
        if board == []:
            return False
        if word == "":
            return True
        self.find = False
        visited=[[0 for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.getWords(board, word, i, j, visited, 0):
                        return True
        return False
    def getWords(self,board,word,i, j, visited, pos):
        if pos == len(word):
            return True
        if i==len(board) or i<0 or j==len(board[0]) or j<0 or board[i][j]!=word[pos] or visited[i][j]==1:
            return False

        visited[i][j]=1
        res = self.getWords(board, word, i, j + 1, visited, pos + 1) \
                or self.getWords(board, word, i, j - 1, visited, pos + 1) \
                or self.getWords(board, word, i + 1, j, visited, pos + 1) \
                or self.getWords(board, word, i - 1, j, visited, pos + 1)
        visited[i][j]=0
        return res

c=Solution()
# print c.exist(["ABCE","SFCS","ADEE"],"ABCCED")
# print c.exist(["a"],"ab")
# print c.exist(["ab","cd"],"dbac")
# print c.exist(["CAA","AAA","BCD"], "A")
# Test case:
#["CAA","AAA","BCD"], "AAB"