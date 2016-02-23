class Solution {
public:
    vector<int> findMinHeightTrees(int n, vector<pair<int, int>>& edges) {
          unordered_set<int> nodes;
          vector<set<int>> nodeToOther(n, set<int>{});
          for(auto p : edges){
              nodeToOther[p.first].insert(p.second);
              nodeToOther[p.second].insert(p.first);
          }
          for(int i = 0; i < n; i++)
            nodes.insert(i);
          vector<int> leaf;
          while(true){
              auto res = findLeafAndRemoveNodes(nodeToOther, nodes);
              if(res.empty()) break;
              leaf = res;
          }
          if(nodes.size() == 0)
              return leaf;
          else 
              return vector<int>({*nodes.begin()});
    }
    vector<int> findLeafAndRemoveNodes(vector<set<int>> & nodeToOther, unordered_set<int> & nodes){
        vector<int> toBeDeleted;
        for(const auto & node : nodes )
             if(nodeToOther[node].size() == 1)
                toBeDeleted.push_back(node);
        for(auto node : toBeDeleted){
            nodes.erase(node);
            nodeToOther[*(nodeToOther[node].begin())].erase(node);
        }
        return toBeDeleted;
    }
};
