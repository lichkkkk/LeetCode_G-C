class Solution {
public:
    string removeDuplicateLetters(string s) {
        // using stack
        vector<int>appear(26+6, s.size());
        for(int i = 0; i < s.size(); i++)
            appear[s[i] - 'a'] = i;
        string ret;
        int appearInRet = 0;
        for(int i = 0; i < s.size(); i++){
            if(appearInRet & 1<<(s[i]-'a'))    
                continue;
            while(!ret.empty() && ret.back() > s[i] && appear[ret.back()-'a'] > i){
                appearInRet &= ~ (1<<(ret.back()-'a'));
                ret.pop_back();
            }
            ret.push_back(s[i]);       
            appearInRet |= 1<<(s[i]-'a');
         }
         return ret;
    }
};