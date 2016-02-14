class Solution {
public:
    vector<set<char>> rows_choices, cols_choices, blks_choices;
    stack<pair<int, int>> S;
    vector<vector<char>> b;
    void intial(){
        set<char> choices;
        for(int i = '1'; i <= '9'; i++)
            choices.insert(i);
        for(int i = 0; i < 9; i++){
            rows_choices.push_back(choices);
            cols_choices.push_back(choices);
            blks_choices.push_back(choices);
        }
        for(int i = 0; i < 9; i++)
            for(int j = 0; j < 9; j++)
                if(b[i][j] == '.')
                    S.push(make_pair(i, j));
                else
                    update(i, j, b[i][j]);        
    }
    void update(int i, int j, char c){
        rows_choices[i].erase(c);
        cols_choices[j].erase(c);
        blks_choices[3*(i/3) + j/3].erase(c);
    }
    set<char> intersect(set<char> s1, set<char> s2){
        vector<char> v;
        v.resize(9);
        auto it = set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), v.begin());
        v.resize(it-v.begin());
        return set<char>(v.begin(), v.end());
    }
    void restore(int i, int j, char c){
        rows_choices[i].insert(c);
        cols_choices[j].insert(c);
        blks_choices[3*(i/3) + j/3].insert(c);   
    }
    void solveSudoku(vector<vector<char>>& board) {
        b = board;
        intial();
        dfs();
        board = b;
    }
    bool dfs(){
        if(S.empty()) return true;
        auto t = S.top();
        S.pop();
        int i = t.first;
        int j = t.second;
        set<char> choices = intersect(intersect(rows_choices[i], cols_choices[j]), blks_choices[3*(i/3) + j/3]);
        for(auto c : choices){
            b[i][j] = c;
            update(i, j, c);
            if(dfs()) return true;
            restore(i, j, c);
        }
        S.push(t);
        return false;
    }
};
