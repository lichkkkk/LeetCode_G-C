class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal == 0:
            return True
        numsLeft = list(range(1, maxChoosableInteger+1))
        if sum(numsLeft) < desiredTotal:
            return False
        return self.helper(numsLeft, desiredTotal, {})
    
    def helper(self, numsLeft, totalLeft, cache):
        if totalLeft <= 0:
            return False
        if max(numsLeft) >= totalLeft:
            return True
        
        cacheKey = str(numsLeft)
        if cacheKey not in cache:
            cache[cacheKey] = {}
        elif totalLeft in cache[cacheKey]:
            return cache[cacheKey][totalLeft]
        
        for num in numsLeft:
            updatedNumsLeft = numsLeft.copy()
            updatedNumsLeft.remove(num)
            if not self.helper(updatedNumsLeft, totalLeft - num, cache):
                cache[cacheKey][totalLeft] = True
                return True
        cache[cacheKey][totalLeft] = False
        return False
