class Solution {
public:
    int mySqrt(int x) {
         return (int)sqrt(x);
         //return guess(0, x, x);
    }
    int guess(long l, long h, long x){
        //printf("%d %d \n", l, h);
        if(l == h) return l;
        long long m = l + (h-l)/2;
        if(m == l){
            if(h*h <= x) return h;
            return m;
        }
        if(m*m > x)
            return guess(l, m, x);
        else 
            return guess(m, h, x);
    }
};
