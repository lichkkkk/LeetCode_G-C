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
    bool isValidBST(TreeNode* root) {
        double INF = 1e40;
        double low = - INF;
        double high = INF;
        return isValid(root, low, high);
    }
    bool isValid(TreeNode* root, double low, double high){
        if(!root) return true;
        if(root->val < high && root->val > low)
            return isValid(root->right, root->val, high) &&\
                   isValid(root->left, low, root->val);
        else return false;           
    }
};
