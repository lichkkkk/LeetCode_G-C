class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        curr_row = A[0].copy()
        for i in range(1, len(A)):
            tmp = A[i].copy()
            for j in range(len(tmp)):
                tmp[j] += min(curr_row[max(0, j-1):min(len(curr_row), j+2)])
            curr_row = tmp
        return min(curr_row)
