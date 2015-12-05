/*
 * Can be solved easily with counting sort.
 * To do the sorting in only one pass, we need to maintain two
 * pointers. A little bit like the way we use to solve 2-SUM or 3-SUM.
 * 
 * Running Time: O(n)
 *
 * Chang Li at UC San Diego
 * Dec. 4, 2015
 */

public class Solution {
    public void sortColors(int[] nums) {
   		if(nums == null || nums.length <= 1) {
			return;
		}
		int zeroPos = 0;
		int twoPos = nums.length-1;
		int pos = 0;
		while(pos <= twoPos) {
			if(nums[pos] == 0) {
				exchange(nums, pos, zeroPos);
				zeroPos++;
				pos++;
			}else if(nums[pos] == 2) {
				exchange(nums, pos, twoPos);
				twoPos--;
			}else {
				pos++;
			}
		}
    }

	public void exchange(int[] nums, int i, int j) {
		int tmp = nums[i];
		nums[i] = nums[j];
		nums[j] = tmp;
	}
}

