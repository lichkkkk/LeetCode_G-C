class Solution:
    def mincostTickets2(self, days: List[int], costs: List[int]) -> int:
        return self.helper(days, costs, 0, {})
    
    # recursion + memorization solution
    def helper(self, days, costs, start_pos, cache):
        if start_pos == len(days):
            return 0
        if start_pos in cache:
            return cache[start_pos]
        option_1 = costs[0] + self.helper(days, costs, start_pos + 1, cache)
        option_2_pos = start_pos
        while option_2_pos < len(days) and days[option_2_pos] - days[start_pos] < 7:
            option_2_pos += 1
        option_2 = costs[1] + self.helper(days, costs, option_2_pos, cache)
        option_3_pos = option_2_pos
        while option_3_pos < len(days) and days[option_3_pos] - days[start_pos] < 30:
            option_3_pos += 1
        option_3 = costs[2] + self.helper(days, costs, option_3_pos, cache)
        res = min(option_1, option_2, option_3)
        cache[start_pos] = res
        return res
    
    # table filling solution
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        table = [0] * 366
        dayset = set(days)
        for i in range(364, -1, -1):
            if i + 1 in dayset:
                option_1 = costs[0] + table[i + 1]
                option_2 = costs[1] + table[min(i + 7, 365)]
                option_3 = costs[2] + table[min(i + 30, 365)]
                table[i] = min(option_1, option_2, option_3)
            else:
                table[i] = table[i + 1]
        return table[0]
