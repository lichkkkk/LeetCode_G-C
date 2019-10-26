/**
 * 1011. Capacity To Ship Packages Within D Days
 * Jun. 23, 2019 Google NYC
 */
class Solution {
    public int shipWithinDays(int[] weights, int D) {
        int maxWeight = 0;
        int sumWeights = 0;
        for (int w : weights) {
            maxWeight = Math.max(w, maxWeight);
            sumWeights += w;
        }
        int low = Math.max(maxWeight, sumWeights/D);
        if (trytry(weights, D, low)) {
            return low;
        }
        int up = sumWeights;
        // Okay, start binary search
        while (up - low > 1) {
            int mid = (up + low) / 2;
            if (trytry(weights, D, mid)) {
                up = mid;
            } else {
                low = mid;
            }
        }
        return up;
    }
    
    private static boolean trytry(int[] weights, int D, int size) {
        int days = 1;
        int currentLoad = 0;
        for (int i=0; i<weights.length; i++) {
            if (currentLoad + weights[i] > size) {
                days += 1;
                currentLoad = 0;
            }
            currentLoad += weights[i];
        }
        return days <= D;
    }
}
