"""
22. Generate Parentheses
licha@London, Apr. 3rd, 2020
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res_set = set()
        curr_res = []
        self.helper(n, n, curr_res, res_set)
        return res_set
    
    def helper(self, n_left, n_right, curr_res, res_set):
        if n_right < n_left:
            return
        if n_left == n_right == 0:
            res_set.add("".join(curr_res))
            return
        if n_left > 0:
            curr_res.append('(')
            self.helper(n_left - 1, n_right, curr_res, res_set)
            curr_res.pop()
        if n_right > 0:
            curr_res.append(')')
            self.helper(n_left, n_right - 1, curr_res, res_set)
            curr_res.pop()
