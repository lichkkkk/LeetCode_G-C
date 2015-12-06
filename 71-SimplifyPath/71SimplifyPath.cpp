class Solution {
public:
    string simplifyPath(string path) {
        vector<string> h;
        int i = -1; 
        while(++i < path.size()){
            string s;
            while(i < path.size() && path[i] == '/') i++;
            while(i < path.size() && path[i] != '/') {
                s.push_back(path[i]);
                i++;
            }
            h.push_back(s);
        }
        vector<string> p;
        for(auto it : h)
            if(it == ".."){
                if(!p.empty())
                    p.pop_back();
                continue;
            }else if(it == "."){
                continue;
            }else{
                if(!it.empty())
                    p.push_back(it);
            }
        string res("/");
        for(auto it : p)            
            res += it + "/";
        if(res.size()>1)
            res.resize(res.size() - 1);
        
        return res;
        
    }
};
