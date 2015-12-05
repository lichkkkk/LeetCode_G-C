class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, int> dict;
        vector<vector<string>> res;
        int cnt = 0;
        for(auto str : strs){
            string s(str);
            sort(s.begin(), s.end());
            if(dict.find(s) != dict.end()){
                res[dict[s]].push_back(str); 
            }else{
                res.push_back(vector<string>({str}));
                dict[s] = cnt;
                ++cnt;
            }
        }
        
        for(auto & strVec : res)
            sort(strVec.begin(), strVec.end());
        
        return res;
    }
    
};
