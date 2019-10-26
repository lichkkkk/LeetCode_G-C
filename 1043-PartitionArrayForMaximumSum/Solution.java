/**
 * 1043. Partition Array for Maximum Sum
 * Jun. 23, 2019 Google NYC
 */
class Solution {
    public int maxSumAfterPartitioning(int[] A, int K) {
      Map<Integer, Integer> cache = new HashMap<>();
      return helper(A, K, 0, cache);  
    }
  
    private static int helper(int[] A, int K, int startIndex, Map<Integer, Integer> cache) {
      if (startIndex >= A.length) {
        return 0;
      }
      if (cache.containsKey(startIndex)) {
        return cache.get(startIndex);
      }
      int maxInThisPartition = -1;
      int max = -1;
      for (int i=startIndex; i<Math.min(startIndex+K, A.length); i++) {
        maxInThisPartition = Math.max(maxInThisPartition, A[i]);
        max = Math.max(max, maxInThisPartition * (i-startIndex+1) + helper(A, K, i+1, cache));
      }
      cache.put(startIndex, max);
      return max;
    }
}
