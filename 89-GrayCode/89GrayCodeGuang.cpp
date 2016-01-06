class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> res;
        if(n == 0) return vector<int>({0});
        auto t = grayCode(n-1);
        join(res, t, 0, 1);
        join(res, t, 1<<(n-1), 0);
        return res;
    }
    
    
    void join(vector<int> & v1, vector<int> & v2, int factor, int dir){
        int s = v2.size();
        if(dir == 0)// reverse
            while(s){
                v1.push_back(v2[s-1] | factor);
                s--;
            }
        else{
            int i = 0;
            while(i < s){
                v1.push_back(v2[i] | factor);
                i++;
            }
        }
    }
};
