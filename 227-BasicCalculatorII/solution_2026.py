class Solution:
    def tokenize(self, s: str) -> list[str]:
        """
        '1 + 2 / 3' -> ['+', '1', '+', '2', '/', '3']
        """
        s = s.replace(' ', '')
        tokens = []
        curr = []
        for c in s:
            if not c.isdigit():
                if curr:
                    tokens.append(''.join(curr))
                curr.clear()
                tokens.append(c)
            else:
                curr.append(c)
        tokens.append(''.join(curr))
        return tokens

    def calculate(self, s: str) -> int:
        s = self.tokenize('+' + s)
        # print(s)
        stack = []
        for token in s:
            if token in '+-/*':
                stack.append(token)
            else:
                # is a non-heading number
                op_ch = stack.pop()
                num = int(token)
                match op_ch:
                    case '*':
                        last_num = stack.pop()
                        stack.append(last_num * num)
                    case '/':
                        last_num = stack.pop()
                        stack.append(int(last_num / num))
                    case '-':
                        stack.append(-1 * num)
                    case '+':
                        stack.append(num)
                    case _:
                        raise ValueError('invalid op', op_ch)
        # print(stack)
        return sum(stack)
