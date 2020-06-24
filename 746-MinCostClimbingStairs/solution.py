class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
      mCost = [0] * len(cost)
      mCost[0] = cost[0]
      mCost[1] = cost[1]
      for i in range(2, len(cost)):
        mCost[i] = cost[i] + min(mCost[i-1], mCost[i-2])
      return min(mCost[-1], mCost[-2])
