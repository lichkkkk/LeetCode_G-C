class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper('', n, n, res)
        return res

    def helper(self, curr_str: str, left_budget: int, right_budget: int, res: [str]) -> None:
        if left_budget == 0 and right_budget == 0:
            res.append(curr_str)
        else:
            if left_budget > 0:
                self.helper(curr_str + '(', left_budget-1, right_budget, res)
            if right_budget > 0 and right_budget > left_budget:
                self.helper(curr_str + ')', left_budget, right_budget-1, res)
