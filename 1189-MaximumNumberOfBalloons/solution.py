class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        cnt['l'] //= 2
        cnt['o'] //= 2
        return min(cnt[ch] for ch in 'balloon')
