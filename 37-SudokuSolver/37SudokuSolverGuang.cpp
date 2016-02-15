class Solution {
public:
    vector<int> rows_choices, cols_choices, blks_choices;
    stack<pair<int, int>> S;
    vector<vector<char>> b;
    void intial(){
        int choices = 0b111111111;
        for(int i = 0; i < 9; i++)
            rows_choices.push_back(choices);
        blks_choices = cols_choices = rows_choices;
        for(int i = 0; i < 9; i++)
            for(int j = 0; j < 9; j++)
                if(b[i][j] == '.')
                    S.push(make_pair(i, j));
                else
                    update(i, j, b[i][j]);        
    }
    void update(int i, int j, char c){
        int num = ~(1 << (c - '1'));
        rows_choices[i] &= num;
        cols_choices[j] &= num;
        blks_choices[3*(i/3) + j/3] &= num;
    }
    void restore(int i, int j, char c){
        int num = 1 << (c - '1');
        rows_choices[i] |= num;
        cols_choices[j] |= num;
        blks_choices[3*(i/3) + j/3] |= num;   
    }
    bool dfs(){
        if(S.empty()) return true;
        auto t = S.top();
        S.pop();
        int i = t.first;
        int j = t.second;
        int choices = rows_choices[i] & cols_choices[j] & blks_choices[3*(i/3) + j/3];
        for(int k = 0; k < 9; k++){
            char c = k + '1';
            if(!((choices>>k)&0x1)) continue;
            b[i][j] = c;
            update(i, j, c);
            if(dfs()) return true;
            restore(i, j, c);
        }
        S.push(t);
        return false;
    }
    void solveSudoku(vector<vector<char>>& board) {
        // compiler complain if reference is used here do not know y
        b = board;
        intial();
        dfs();
        board = b;
    }    
};
