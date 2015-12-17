class Solution {
public:
    void run(vector<int>& label, vector<string>& words){
        for(int i = 0; i < words.size(); i++){
            for(int j = 0; j < words[i].size(); ++j)
                label[i] |=  1<<(words[i][j]-'a');
        }
    }
    int maxProduct(vector<string>& words) {
        vector<int>label(words.size(), 0);
        run(label, words);
        int ret = 0;
        for(int i = 0; i < words.size(); i++)
            for(int j = i+1; j < words.size(); ++j)
                ret = max(ret, label[i]&label[j]?0:(int)words[i].size()*(int)words[j].size());
        return ret;
    }
};