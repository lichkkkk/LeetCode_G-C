class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> res;
        res.resize(num+1);
        int l = 1;
        res[0] = 0;
        int start = 1;
        while(start <= num){
            for(int i = 0; i < l && start+i <= num; i++)
                res[start+i] = res[i] + 1;
            start += l;
            l *= 2;
        }
        return res;
    }
};
