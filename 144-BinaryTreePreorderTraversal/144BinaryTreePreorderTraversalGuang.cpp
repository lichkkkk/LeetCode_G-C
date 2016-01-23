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
    vector<int> preorderTraversal(TreeNode* root) {
        stack<TreeNode *> s;
        s.push(root);
        vector<int> ret;
        while(!s.empty()){
            auto p = s.top();
            s.pop();
            if(p) ret.push_back(p->val);
            else continue;
            s.push(p->right);
            s.push(p->left);
        }
        return ret;
    }
};
