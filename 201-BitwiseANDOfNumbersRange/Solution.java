class Solution {
    public int rangeBitwiseAnd(int m, int n) {
        int res = 0;
        int mask = 1 << 31;
        for (int i=0; i<32; i++) {
            int mi = m & mask;
            int ni = n & mask;
            if (mi != ni) {
                break;
            } else {
                res |= mask & mi;
            }
            mask >>= 1;
        }
        return res;
    }
}
