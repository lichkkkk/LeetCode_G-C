class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        value = numExchange * numBottles // (numExchange - 1)
        residue = numExchange * numBottles % (numExchange - 1)
        return value if residue else value - 1
