public class Solution {
    // This peoblem is winderful. At the first glance, it could be a classic DP problem, for every time you make a choice, 
    // the size of the problem will reduce one. 
    // The recursion function may like this: 
    //      F(n1,n2,..,nk) = max {F(n1, n2, .., ni-1, ni+1, …, nk) + ni-1 * ni * ni+1}
    // In this way it could be hard to express the state, and there will be 2^n states --- too many
    // So, instead of choosing the one to brust first, we can choose the one to brust last
    // Then states of the DP becomes O(n^2)
    //
    // Running Time: O(n^2)
    // Chang Li at UC San Diego
    // Dec. 5, 2015
    
    public int maxCoins(int[] nums) {
		// table[i][j] means the max coins from i to j (include i, j)
    		int[][] table = new int[nums.length][nums.length];
	    	for(int[] tmp : table) Arrays.fill(tmp, -1);
	    	return helper(nums, 0, nums.length-1, table);
    }

	public int helper(int[] nums, int start, int end, int[][] table) {
		if(start > end) return 0;
		// Memorization
        if(table[start][end] != -1) return table[start][end];
        int max = -1;
        // Divide & Conquer
        int leftNum = (start==0)?1:nums[start-1];
        int rightNum = (end==nums.length-1)?1:nums[end+1];
        for(int i=start; i<=end; i++) {
        	max = Math.max(max, helper(nums, start, i-1, table) + leftNum*nums[i]*rightNum + helper(nums, i+1, end, table));
        }
        table[start][end] = max;
        return max;
    }
}
