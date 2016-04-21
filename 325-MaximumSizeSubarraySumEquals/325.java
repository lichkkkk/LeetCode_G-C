public class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
        int[] pre_sum = new int[nums.length+1];
        pre_sum[0] = 0;
        int max_len = 0;
        for (int i = 0; i<nums.length; i++) {
            pre_sum[i+1] = pre_sum[i]+nums[i];
        }
        HashMap<Integer,Integer> dic = new HashMap<Integer,Integer>();
        for (int j=0;j<pre_sum.length;j++) {
            if (!dic.containsKey(pre_sum[j])) {
                dic.put(pre_sum[j],j);
            }
            int need = pre_sum[j]-k;
            if (dic.containsKey(need)) {
                max_len = Math.max(max_len, j - dic.get(need));
            }
        }
        return max_len;
    }
}