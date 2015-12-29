/**
 * Add a header to store the length of each string.
 *
 * Chang Li
 * Dec. 29, 2015
 */

class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string res = "";
        for(auto str = strs.begin(); str < strs.end(); str++) {
            int len = (*str).size();
            res.append(to_string(len) + "#" + (*str));
        }
        return res;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> res;
        int pos = 0;
        int len;
        while((len=parse_len(s, pos)) != -1) {
            res.push_back(s.substr(pos, len));
            pos += len;
        }
        return res;
    }
    
    int parse_len(string s, int& pos) {
        if(pos >= s.size()) {
            return -1;
        }
        int len = 0;
        while(s[pos] != '#') {
            len = len*10 + s[pos] - '0';
            pos++;
        }
        pos++;
        return len;
    }
    
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));
