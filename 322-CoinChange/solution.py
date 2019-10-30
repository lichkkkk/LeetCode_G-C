"""
Key Points:
    1. The easiest way to solve this is to check all possible combinations, which is too slow
    2. Because CoinChange(N) = min{CoinChange(N-coin) + 1} for all coin in coins, we can use
    a recursion to solve this problem. But if we do not do any optimization, this is equal to
    the check-all-combination approach above.
    3. We can use a Map to memorize all CoinChange(N) results we get during the process, so we
    do not need to compute them more than one time. So it will be much faster. This approach
    is call memorization-based Dynamic Programming. You do not need to understand what it is
    at this moment. But do remember to metion this word during the explanation.
    4. The specific implementation is the code version of the equation mentioend in (2) and the
    use of the Map.
    5. At the beginning of the helper, we check several special cases and return some simple
    answer for them, this is to prevent them entering an endless loop.

How to improve:
    1. We are using recursion here. If the amount is too large, we may get a stack overflow
    error, since the depth of recursion will be very high. So, we can use a while look to replace
    the recursion.
    2. We can sort the coins and make it from large to small. This is kind of like the greedy
    algorithm, but because generally large value coin will be more likely to be used, this
    can potentially make the code faster.
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        return self.coinChangeHelper(coins, amount, {}) # directly call the helper, use an empty map as the initial cache
        
    # return the min # of coins we will need for amount, return -1 if impossible
    def coinChangeHelper(self, coins, amount, cache):
        """
        :type coins: List[int]
        :type amount: int
        :type cache: Map<int, int>
        :rtype: int
        """
        if amount < 0: # if amount < 0, then it's impossible to make the change
            return -1;
        if amount == 0: # if amount = 0, then the answer is 0, since no further coin change is required
            return 0
        if amount in cache: # if we computed this amount before, directly return the memorized result
            return cache[amount]
        # if we go here, then we have to compute the answer by ourselves
        minCount = -1 # use this variable to track the minimun count of coins we will need, by default set it as -1
        for coin in coins: # iterate over all coins
            # for a certain coin, first compute what's the min # of coins we will need for 'amount-coin'
            # if the answer for 'amount-coin' is N, then we can do N=1 for amount(though this may not be the minimun)
            count = self.coinChangeHelper(coins, amount-coin, cache)
            if count == -1: # if it's impossible to get changes for amount-coin, just directly go to the next coin in the list
                pass
            # otherwise, if this is the first solution we get(minCount=-1), or this is the best so far(count+1<minCount)
            # then we update the best min #
            elif minCount == -1 or count + 1 < minCount:
                minCount = count + 1
        # after we finish the loop, we put the fresh result into our records for potential future use. Note minCount may = -1
        cache[amount] = minCount
        return minCount
