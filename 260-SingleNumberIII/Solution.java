/**
 * 260. Single Number III
 * Chang Li
 * Jan. 6, 2015
 */

public class Solution {
    public int[] singleNumber(int[] nums) {
        int diff = 0;
        for(int num : nums) {
            diff ^= num;
        }
        // Get its last set bit
        diff &= - diff;
        int[] res = new int[2];
        for(int num : nums) {
            if((num & diff) != 0) {
                res[0] ^= num;
            }else {
                res[1] ^= num;
            }
        }
        return res;
    }
}