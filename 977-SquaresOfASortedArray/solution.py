class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if A[0] >= 0:
            return [A[i]**2 for i in range(len(A))]
        elif A[-1] <= 0:
            return [A[-(i+1)]**2 for i in range(len(A))]
        
        l, r = 0, len(A)-1
        res = [0] * len(A)
        pos = len(A) - 1
        while l <= r:
            if abs(A[l]) >= abs(A[r]):
                res[pos] = A[l]**2
                l += 1
            else:
                res[pos] = A[r]**2
                r -= 1
            pos -= 1
        return res
