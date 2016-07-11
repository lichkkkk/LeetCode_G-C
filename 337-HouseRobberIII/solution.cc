/**
 * 337. House Robber III
 * 
 * Chang Li @ Mountain View
 * Jul. 10, 2016
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
    int rob(TreeNode* root) {
        if (root == nullptr) return 0;
        auto it = income_.find(root);
        if (it == income_.end()) {
            const vector<TreeNode*>& children = getChildren(vector<TreeNode*>{root});
            const vector<TreeNode*>& grandSon = getChildren(children);
            income_[root] = max(root->val+computeIncome(grandSon), computeIncome(children));
        }
        return income_[root];
    }
    
private:
    int computeIncome(const vector<TreeNode*> nodes) {
        int income = 0;
        for (auto node : nodes) {
            income += rob(node);
        }
        return income;
    }

    vector<TreeNode*> getChildren(const vector<TreeNode*> nodes) {
        vector<TreeNode*> children;
        for (auto node : nodes) {
            if (node->left != nullptr) {
                children.push_back(node->left);
            }
            if (node->right != nullptr) {
                children.push_back(node->right);
            }
        }
        return children;
    }
    
    unordered_map<TreeNode*, int> income_;
};
