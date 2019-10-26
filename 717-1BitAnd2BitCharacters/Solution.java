/**
 * 717. 1-bit and 2-bit Characters
 * Jun. 26, 2019 Google NYC
 */
class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        int i = 0;
        while (i < bits.length - 1) {
            i += bits[i] == 1 ? 2 : 1;
        }
        return i == bits.length - 1;
    }
}
