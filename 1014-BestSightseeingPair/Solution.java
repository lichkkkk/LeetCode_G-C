/**
 * 1014. Best Singtseeing Pair
 * Jun. 22, Google NYC
 */
class Solution {
    public int maxScoreSightseeingPair(int[] A) {
      if (A == null || A.length <= 1) {
        return 0;
      }
      int best = 0;
      int leftValue = A[0];
      for (int i =1; i<A.length; i++) {
        int rightValue = A[i];
        int currentPair = leftValue + rightValue - 1;
        best = Math.max(best, currentPair);
        if (leftValue > rightValue) {
          leftValue = leftValue - 1;
        } else {
          leftValue = rightValue;
        }
      }
      return best;
    }
}
