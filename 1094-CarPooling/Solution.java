/**
 * 1094. Car Pooling
 * Jun. 25 Google NYC
 */
class Solution {
    
    static final int MAX_STOP = 1000;
    
    public boolean carPooling(int[][] trips, int capacity) {
        int[] stops = new int[MAX_STOP];
        for (int[] trip : trips) {
            stops[trip[1]] += trip[0];
            stops[trip[2]] -= trip[0];
        }
        for (int i=0; i<stops.length && capacity >= 0; i++) {
            capacity -= stops[i];
        }
        return capacity >= 0;
    }
}
