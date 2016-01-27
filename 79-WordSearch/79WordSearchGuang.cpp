class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        if(!board.size() && word.size())
            return false;
        vector<vector<int> > path(board.size(), vector<int>(board[0].size(), 0));
        for(int i = 0; i < board.size(); i++)
            for(int j = 0; j < board[0].size(); j++)
                if(dfs(word, i, j, board, path)) return true;
        return false;        
    }
    bool dfs(string word, int i, int j, vector<vector<char>>& board, vector<vector<int>>& path){
        if(word.size() == 0) return true;
        if(i>=0 && i < board.size() && j>= 0 && j< board[0].size() && path[i][j] == 0 && board[i][j] == word[0]){
            path[i][j] = 1;
            for(int p = i-1; p <= i+1; p++)
                for(int q = j-1; q <= j+1 ; q++)
                        if((p+q-(i+j) == -1 || p+q -(i+j) == 1 ) && dfs(word.substr(1, word.size()), p, q, board, path) == true) 
                            return true;
            path[i][j] = 0;    
        }        
        return false;
    }
};
