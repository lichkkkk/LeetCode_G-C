/**
 * 134. Gas Station
 * Tag: Array
 *      Kind of interesting. Like doing an integration in Math but is more tricky.
 *      My code is a little bit massy. Sorry about that.
 * Running Time: O(n)
 * Chang Li at UC San Diego
 * Jan. 23, 2016
 */

public class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int gasLeft = 0;
        int startPos = 0;
        int currPos = 0;
        
        while(true) {
            // Have enough gas. Just move forward
            do {
                gasLeft += (gas[currPos] - cost[currPos]);
                currPos = (currPos + 1) % gas.length;
            }while(gasLeft >= 0 && currPos != startPos);
            
            // Success. Already drive a loop
            if(gasLeft >= 0 && currPos == startPos) {
                return startPos;
            // Failed. And No need to try the other startPos
            }else if(currPos <= startPos) {
                return -1;
            // Failed. Try to set the next node as the startPos
            }else {
                gasLeft = 0;
                startPos = currPos;
            }
        }
    }
}
