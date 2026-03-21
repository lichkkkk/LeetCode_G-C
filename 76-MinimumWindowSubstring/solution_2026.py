from collections import deque

class Solution:
    # can use two pointers instead of deque
    def minWindow(self, s: str, t: str) -> str:
        dq = deque()
        shortest_s = ''
        balance = {}
        missing_char_set = set(t)
        # step 1: process t
        for ch in t:
            if ch not in balance:
                balance[ch] = 0
            balance[ch] -= 1
        # step 2: go through s
        for ch in s:
            dq.append(ch)
            if ch not in balance:
                continue
            balance[ch] += 1
            # maybe flip state -> this will only happen once ever
            if missing_char_set and balance[ch] == 0:
                missing_char_set.remove(ch)
            # pop unnecessary chars in the back
            while dq:
                last_ch = dq[0]
                if last_ch not in balance:
                    dq.popleft()
                elif balance[last_ch] > 0:
                    dq.popleft()
                    balance[last_ch] -= 1
                else:
                    break
            if not missing_char_set:
                if not shortest_s or (len(dq) < len(shortest_s)):
                    shortest_s = ''.join(dq)
        return shortest_s
