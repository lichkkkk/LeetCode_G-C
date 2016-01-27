// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int l = 1; int h = n; 
        while(l < h){
            int m = l + (h-l)/2;
            auto b = isBadVersion(m);
            if(b)
                h = m;
            else// ugly here   : another way is try to reduce to two cases n == 1 or n == 2
                l = m==l? m+1: m;
        }
        return l;
    }
};
