__author__ = 'liuxiyun'
# Dynamic Programming
# sum_cost[n][k] = min(sum_cost[n-1][i] for i in range(k) and i!=k)
# O(nkk)
class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if costs==[]:
            return 0
        sum_cost = costs[:][:]
        for i in range(1,len(costs)): # from the 2nd house
            for k in range(len(costs[0])):# this house's color
                mincost=27000000
                for kk in range(len(costs[0])): # n-1 house's color
                    if kk == k: # cannot be same colar
                        continue
                    mincost=min(mincost, sum_cost[i-1][kk]+costs[i][k])
                sum_cost[i][k] = mincost
        print sum_cost
        return min(sum_cost[-1])

#O(nk)
# We can use min1 and min2 to track the indices of the 1st and 2nd smallest cost till previous house,
# if the current color's index is same as min1, then we have to go with min2,
# otherwise we can safely go with min1.

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if costs==[]:
            return 0
        sum_cost = costs[:][:]
        for i in range(1,len(costs)): # from the 2nd house
        # find the two smallest cost for painting n-1 houses
            smallest = []
            min_val = min(sum_cost[i-1])
            for index in range(len(sum_cost[i-1])):
                if sum_cost[i-1][index] == min_val:
                    smallest.append(index)
            if len(smallest) < 2:
                smallest2=sum_cost[i-1][:] # copy the list
                smallest.append(smallest2.pop(smallest[0]))

            for k in range(len(costs[0])):# this house's color is k
                if smallest[0] != k:
                    sum_cost[i][k] = sum_cost[i-1][smallest[0]]+costs[i][k]
                else:
                    sum_cost[i][k] = sum_cost[i-1][smallest[1]]+costs[i][k]
                print sum_cost[i][k]
        print sum_cost
        return min(sum_cost[-1])