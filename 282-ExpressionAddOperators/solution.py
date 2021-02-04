# started with DP and actually just a DFS, many corner cases
class Solution:
    
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        self.helper(num, [], 0, 1, target, res)
        return res
    
    def helper(self, s, stack, curr_value, last_value, target, res):
        # print(s, stack, curr_value, last_value, target, res)
        if len(s) == 0:
            if curr_value == target:
                rs = ''.join(stack)
                rs = rs[1:] if rs[0] == '+' else rs
                res.append(rs)
            return
        for i in range(1, len(s)+1):
            if s[0] == '0' and i > 1:
                break
            num = int(s[:i])
            for op in ['+', '-', '*']:
                if len(stack) == 0 and op != '+':
                    continue
                if op == '*':
                    n_curr_value = curr_value + last_value * (num - 1)
                    n_last_value = last_value * num
                elif op == '+':
                    n_curr_value = curr_value + num
                    n_last_value = num
                else:
                    n_curr_value = curr_value - num
                    n_last_value = -1 * num
                stack.append(op + s[:i])
                self.helper(s[i:], stack, n_curr_value, n_last_value, target, res)
                stack.pop()
