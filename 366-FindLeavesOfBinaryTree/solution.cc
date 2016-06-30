/**
 * 366. Find Leaves of Binary Tree
 *    Cost 0 ms
 * Chang Li @ Mountain View
 * Jun. 29, 2016
 * 
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> findLeaves(TreeNode* root) {
        vector<vector<int>> res;
        
        if (root != nullptr) {
            dfs(res, root);
        }
        
        return res;
    }
    
    int dfs(vector<vector<int>>& res, TreeNode* root) {
        
        int distance_2_leaf; 
        
        if (root->left == nullptr && root->right == nullptr) {
            distance_2_leaf = 0;
        } else if (root->left != nullptr && root->right != nullptr) {
            distance_2_leaf = max(dfs(res, root->left), dfs(res, root->right)) +1;
        } else if (root->left != nullptr) {
            distance_2_leaf = dfs(res, root->left) +1;
        } else {
            distance_2_leaf = dfs(res, root->right) +1;
        }
        
        // printf("%d - %d\n", root->val, distance_2_leaf);
        
        if (res.size() == distance_2_leaf) {
            res.push_back(vector<int>());
        }
        res[distance_2_leaf].push_back(root->val);
        
        return distance_2_leaf;
    }
};
