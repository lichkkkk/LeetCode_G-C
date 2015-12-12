/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {
        TreeLinkNode * cur, *next, *nextLevelStart = root;
        // level 1 is cleared
        if(root) root->next = NULL;
        // from level i to level i+1
        // level i is alerady processed, using next pointer in i level to proceed
        // level i+1 starts from nextLevelStart
        while(cur = nextLevelStart){ // level i -> i+1

            // find first non-leaf node for level i+1
            while(cur && (!cur->left) && (!cur->right)) cur = cur->next; 
            if(cur==NULL) return; // last level
            
            if(cur->left) nextLevelStart = cur->left;
            else if(cur->right) nextLevelStart = cur->right;

            while(cur){
				// skip no child node
				next = cur->next;
				while (next && next->left == NULL && next->right == NULL) {
					next = next->next;
				}

                //find next for cur's child
                TreeLinkNode * nextChild = NULL;
                if(next != NULL){
                    if(next->left) nextChild = next->left;
                    else if(next->right) nextChild = next->right;
                }
                //link to next
                if(cur->left){
                    if(cur->right) cur->left->next = cur->right;
                    else cur->left->next = nextChild;
                }
				if(cur->right)
					cur->right->next = nextChild;
        
                if(nextChild == NULL) break;
                cur = next;
            }
        }
    }
};
