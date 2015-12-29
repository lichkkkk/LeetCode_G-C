/**
 * A naive solution with memorization.
 *
 * Chang Li
 * Dec. 29, 2015
 */

public class Solution {
    public int coinChange(int[] coins, int amount) {
        Arrays.sort(coins);
        int[][] table = new int[coins.length][amount+1];
        return helper(table, coins, 0, amount);
    }
    
    public int helper(int[][] table, int[] coins, int start, int amount) {
        if(amount == 0) {
            return 0;
        }else if(start == coins.length || coins[start] > amount) {
            return -1;
        }
        if(table[start][amount] != 0) {
            return table[start][amount];
        }
        int usedSum = 0;
        int usedNumber = 0;
        int min = amount + 1;
        while(usedSum <= amount) {
            int subRes = helper(table, coins, start+1, amount-usedSum);
            if(subRes != -1) {
                min = Math.min(min, usedNumber + subRes);
            }
            usedSum += coins[start];
            usedNumber += 1;
        }
        if(min == amount + 1) {
            table[start][amount] = -1;
            return -1;
        }else {
            table[start][amount] = min;
            return min;
        }
    }
}
