class Solution {
public:
    string convertToTitle(int n) {
        // int c = n%26 - 1 + 'A';
        // string ret;
        // if(c == 'A'-1) c = 'Z';
        // ret.push_back((char)c);
        // if(n <= 26) return ret;
        // return convertToTitle(n/26 - (c=='Z'? 1 : 0)) + ret;
    
    
        string ret;
        do{
           int c = n%26 - 1 + 'A';
           if(c == 'A'-1) c = 'Z';
           ret.push_back((char)c);
           n = n/26 - (c=='Z'? 1 : 0);
        }while(n > 0);
        reverse(ret.begin(), ret.end());
        return ret;
        
    }
    
    
    
};
