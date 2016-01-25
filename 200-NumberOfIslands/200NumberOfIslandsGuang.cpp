// haha, written long time ago
// stupid 
// and ignorant :)
class Solution {
public:
    int num = 0;
    int numIslands(vector<vector<char>> &grid) {
        
        int M = grid.size();
        if(M == 0) return 0;
        int N = grid[0].size();
        
        if(M*N == 0) return 0;
        
        unsigned int * nodes = (unsigned int * )malloc(M * N * sizeof(unsigned int));
        
        memset(nodes, 0, M*N*sizeof(unsigned int));

        for (int i = 0; i < grid.size(); ++i)
        {
           for (int j = 0; j < grid[0].size(); ++j)
           {
              if( grid[i][j] == '1' && nodes[ i*grid[0].size() + j] == 0){
                  ++num;
                  DFS_Mark(grid, nodes, i , j, num);
               }
           }
        }

        free(nodes);
        return num;

    }
    void DFS_Mark(vector<vector<char>> & grid, unsigned int * nodes, int i, int j, int color){
         if ( i >= 0 && i < grid.size() && j >=0  && j < grid[0].size() && grid[i][j] == '1' && (nodes[ i*grid[0].size() + j] == 0))
         {
            nodes[ i*grid[0].size() + j] = color;
            DFS_Mark(grid, nodes, i - 1, j, color);
            DFS_Mark(grid, nodes, i + 1, j, color);
            DFS_Mark(grid, nodes, i, j + 1, color);
            DFS_Mark(grid, nodes, i, j - 1, color);
         }

    }
};
