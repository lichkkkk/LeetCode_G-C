class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        return self.coinChangeHelper(coins, amount, {})
        
    def coinChangeHelper(self, coins, amount, cache):
        """
        :type coins: List[int]
        :type amount: int
        :type cache: Map<int, int>
        :rtype: int
        """
        if amount < 0:
            return -1;
        if amount == 0:
            return 0
        if amount in cache:
            return cache[amount]
        minCount = -1
        for coin in coins:
            count = self.coinChangeHelper(coins, amount-coin, cache)
            if count != -1 and ( minCount == -1 or count + 1 < minCount):
                minCount = count + 1
        cache[amount] = minCount
        return minCount
