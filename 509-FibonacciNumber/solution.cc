class Solution {
public:
    int fib(int n) {
        if (n < 2) return n;       
        int n1 = 0;
        int n2 = 1;
        for (int i=0; i<n-1; i++) {
            int tmp = n1 + n2;
            n1 = n2;
            n2 = tmp;
        }
        return n2;
    }
};
