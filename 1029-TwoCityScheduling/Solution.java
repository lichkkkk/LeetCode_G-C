/**
 * 1029. Two City Scheduling
 * Jun. 25, 2019 Google NYC
 */
class Solution {
    public int twoCitySchedCost(int[][] costs) {
        Arrays.sort(costs, (a, b) -> (a[0]-a[1]) - (b[0]-b[1]));
        int res = 0;
        for (int i=0; i<costs.length/2; i++) {
            res += costs[i][0] + costs[i+costs.length/2][1];
        }
        return res;
    }
}
