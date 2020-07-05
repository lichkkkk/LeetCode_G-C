class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        table = [[9] * 3 for _ in range(3)]
        kr, kc = king[0], king[1]
        for r, c in queens:
            if kr == r or kc == c or abs(r-kr) == abs(c-kc):
                r_offset, c_offset = (r-kr)//max(1,abs(r-kr))+1, (c-kc)//max(1,abs(c-kc))+1
                distance = max(abs(r-kr), abs(c-kc))
                table[r_offset][c_offset] = min(table[r_offset][c_offset], distance)
        # print(table)
        res = []
        for r in range(3):
            for c in range(3):
                if table[r][c] == 9:
                    continue
                res.append([kr+table[r][c]*(r-1), kc+table[r][c]*(c-1)])
        return res

# The code above is too complicated
# Use a BFS-similar approach can be better
