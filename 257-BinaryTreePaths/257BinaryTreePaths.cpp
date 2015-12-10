/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 vector<string> res;
 vector<int> path;
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        res.clear();
        preOrder(root);
        return res;
    }
    string intVectorToString(vector<int> & v){
        string res;
        for(auto i : v){
            res += to_string(i) + "->";
        }
        if(res.size()) return string(res.begin(), res.end()-2);
        return res;
    }
    void preOrder(TreeNode* root){
        if(root){
            path.push_back(root->val);
            if(root->left) preOrder(root->left);
            // bad implementations, leave for future
            if((!root->left) && (!root->right)) res.push_back(intVectorToString(path));
            if(root->right) preOrder(root->right);
            path.pop_back();
        }
    }
};
