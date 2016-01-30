class Solution {
public:
    int numDecodings(string s) {
        int len = s.size();
        if(len == 0) return 0;
        vector<int> w(len+1, 1);
        if(s[len-1] < '1' || s[len-1] > '9') 
            w[len-1] = 0;
        int i = len - 2;
        while(i >= 0){
            // w[i] =   w[i+1]  +  s(i, i+1)? w[i+2]
            w[i] = 0;
            if(s[i] >= '1' && s[i] <= '9')
                w[i] = w[i+1];
            int n = 10*(s[i]-'0') + s[i+1] - '0';
            if(n >= 10 && n <= 26)
                w[i] += w[i+2];
            --i;
        }
        return w[0];
    }
    
};
