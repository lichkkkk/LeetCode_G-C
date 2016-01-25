/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int> > levelOrder(TreeNode *root) {
        vector<vector<int> > res;
        levelTraverse(root, 1, res);
        return res;
    }
    void levelTraverse(TreeNode *p, int level, vector<vector<int> >& res){
        if(p==NULL) return;
        if(level > res.size()) res.push_back(vector<int>({p->val}));
        else res[level-1].push_back(p->val);
        levelTraverse(p->left, level+1, res);
        levelTraverse(p->right, level+1, res);
        return;
    }
};
