class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> ret;
        int sz = s.size();
        if(sz > 12) return ret;
        for(int i = 0; i < sz; i++)
            for(int j = i+1; j < sz; j++)
                for(int k = j+1; k < sz-1; k++){
                    string s1 = s.substr(0, i+1);
                    string s2 = s.substr(i+1, j-i);
                    string s3 = s.substr(j+1, k-j);
                    string s4 = s.substr(k+1);
                    if(check(s1) && check(s2) && check(s3) && check(s4))
                        ret.push_back(s1 + "." + s2 + "." + s3 + "." + s4);
                }
        return ret;
    }
    
    bool check(string s){
        int val = stoi(s);
        // printf("%d  %d\n", val, s.size());
        // if(val == 0){
        //     if(s.size() == 1) return true;
        //     else return false;
        // }
        // else{
        //     if(val <= 255) return true;
        //     else return false;
        // }
        
        return val <= 255 ? (val == 0 ? (s.size() == 1 ? true 
                                                      : false) 
                                      : (s[0] == '0' ? false : true)) 
                          : false;
    }
};
