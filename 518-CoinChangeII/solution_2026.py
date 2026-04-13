class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        f(amount, i) = # of ways with amount with coins[:i]
        f(amount, i) = f(amount, i - 1) + f(amount - coins[i-1], i)
        f(_, len(coins)) = 0
        0 <= i <= len(coins)
        f(0, _) = 1
        '''
        table = [[0] * (len(coins) + 1) for _ in range(amount + 1)]
        for i in range(1, len(coins) + 1):
            table[0][i] = 1
        for i in range(len(coins) + 1):
            coin_val = coins[i-1]
            for a in range(1, amount + 1):
                table[a][i] = table[a][i-1] + (table[a-coin_val][i] if a >= coin_val else 0)
        return table[amount][len(coins)]
