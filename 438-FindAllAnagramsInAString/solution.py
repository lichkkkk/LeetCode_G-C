class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        state = Counter(s[:len(p)])
        state.subtract(Counter(p))
        state = {(k, v) for k, v in state.items() if v != 0}
        res = []
        for i in range(len(p), len(s) + 1):
            # print(i, state)
            if len(state) == 0:
                res.append(i - len(p))
            if i >= len(s):
                break
            state[s[i-len(p)]] -= 1
            if state[s[i-len(p)]] == 0:
                del state[s[i-len(p)]]
            state[s[i]] += 1
            if state[s[i]] == 0:
                del state[s[i]]
        return res
