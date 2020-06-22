class Solution:
    
    MOD_BASE = 10**9 + 7
    
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        return self.helper(d, f, target, {})
    
    def helper(self, d, f, target, cache):
        if d == 0 or target == 0:
            return 0
        if d == 1 and 1 <= target <= f:
            return 1
        if (d, target) in cache:
            return cache[(d, target)]
        res = 0;
        for i in range(1, min(target, f + 1)):
            res += self.helper(d - 1, f, target - i, cache)
            res %= self.MOD_BASE
        cache[(d, target)] = res
        return res
