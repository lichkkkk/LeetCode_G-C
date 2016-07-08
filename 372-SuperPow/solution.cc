/**
 * 372. Super Pow
 * 
 * Chang Li @ Mountain View
 * Jul. 7, 2016
 */
class Solution {
public:
    int superPow(int a, vector<int>& b) {
        int residue = 1;
        int sub_mod = a;
        for (auto it=b.end()-1; it>=b.begin(); --it) {
            residue = (residue * pow_mod(sub_mod, *it, 1337)) % 1337;
            sub_mod = pow_mod(sub_mod, 10, 1337);
        }
        return residue;
    }
    
    int pow_mod(int a, int p, int b) {
        int res = 1;
        for (int i=0; i<p; ++i) {
            res = (res * (a % b)) % b;
        }
        return res;
    }
};
