class Solution {
public:
    vector<int> rows_choices, cols_choices, blks_choices;
    vector<pair<int, int>> S;
    vector<vector<char>> b;
    void intial(){
        int choices = 0b111111111;
        for(int i = 0; i < 9; i++){
            rows_choices.push_back(choices);
            cols_choices.push_back(choices);
            blks_choices.push_back(choices);
        }
        for(int i = 0; i < 9; i++)
            for(int j = 0; j < 9; j++)
                if(b[i][j] == '.')
                    S.push_back(make_pair(i, j));
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
    int len(int num){
        int cnt = 0;
        for(int i = 0; i < 9; i++)
            if(num>>i & 0x1)
                ++cnt;
        return cnt;        
    }
        // bool greater(pair<int, int> p1, pair<int, int> p2) const {
        //     int i1, j1, i2, j2;
        //     i1 = p1.first, i2 = p2.first, j1 = p1.second, j2 = p2.second;
        //     int d = len(1);
        //     int c1 = rows_choices[i1] & cols_choices[j1] & blks_choices[3*(i1/3) + j1/3];
        //     int c2 = rows_choices[i2] & cols_choices[j2] & blks_choices[3*(i2/3) + j2/3];
        //     return len(c1) > len(c2);
        // } 
        //get fucked by this stupid function.........f**k off....cannot say a word 
        
    void shuffle(vector<pair<int, int>>& v){
        int number = 100; int index = 0;
        for(int k = 1; k < v.size(); k++){
            auto t = v[k];
            int i = t.first;
            int j = t.second;
            int choices = rows_choices[i] & cols_choices[j] & blks_choices[3*(i/3) + j/3];
            if(len(choices) < number){ 
                index = k;
                number = len(choices);
            }
        }
        swap(v[index], v[v.size()-1]);
    }
    bool dfs(){
        if(S.empty()) return true;
        shuffle(S);
        auto t = S.back();
        S.pop_back();
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
        S.push_back(t);
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
