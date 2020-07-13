# Check https://leetcode.com/problems/russian-doll-envelopes/discuss/82761/Python-O(nlogn)-O(n)-solution-beats-97-with-explanation
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda e: (e[0], -1 * e[1]))
        best_h = []
        for w, h in envelopes:
            pos = bisect.bisect_left(best_h, h)
            if pos == len(best_h):
                best_h.append(h)
            else:
                best_h[pos] = h
        return len(best_h)
