/**
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
    unordered_map<TreeNode*, int> Mcan; 
    unordered_map<TreeNode*, int> Mcannot;
    int rob(TreeNode* root) {
        return try_steal(root, true);
    }
    int try_steal(TreeNode* root, bool can){
        if(root == NULL) return 0;
        int m = 0, n = 0;
        if(can){
            if(Mcan.find(root) != Mcan.end()) 
                m = Mcan[root]; 
            else{
                m = root->val + try_steal(root->left, false) + try_steal(root->right, false);
                Mcan[root] = m;
            }
        }
        if(Mcannot.find(root) != Mcannot.end()) 
            n = Mcannot[root]; 
        else{
            n = try_steal(root->left, true) + try_steal(root->right, true);
            Mcannot[root] = n;
        }
        return max(m, n);
    }
};
