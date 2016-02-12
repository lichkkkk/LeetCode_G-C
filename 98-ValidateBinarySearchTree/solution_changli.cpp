/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 * 
 * 98. Validate Binary Search Tree
 * Tag: Recursion, BST
 * 
 * Chang Li at UC San Diego
 * Feb. 11, 2016
 */
class Solution {
public:

    int lastValue;
    bool isFirst = true;

    bool isValidBST(TreeNode* root) {
        
        if (!root) return true;
        
        // check left branch
        if (root->left) {
            if (!isValidBST(root->left)) {
                return false;
            }
        }
        
        // compare current value to lastValue
        if (isFirst) {
            lastValue = root->val;
            isFirst = false;
        } else if (root->val <= lastValue) {
            return false;
        }
        lastValue = root->val;
        
        // check the right branch
        if (root->right) {
            return isValidBST(root->right);
        } else {
            return true;
        }
    }
};
