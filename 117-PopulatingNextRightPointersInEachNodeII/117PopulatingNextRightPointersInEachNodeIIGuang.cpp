/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  struct TreeLinkNode *left, *right, *next;
 * };
 *
 */
 typedef struct TreeLinkNode * TP;
void connect(struct TreeLinkNode *root) {
    if(!root) return;
    TP nextLevelStart = NULL, last = NULL, p = root;
    while(p){
        if(nextLevelStart == NULL){
            if(p->left) nextLevelStart = p->left;
            else if(p->right) nextLevelStart = p->right;
        }
        if(p->left){
            if(last) last->next = p->left;
            last = p->left;
        }
        
        if(p->right){
            if(last) last->next = p->right;
            last = p->right;
        }
        if(p->next) p = p->next;
        else {
            p = nextLevelStart;
            last = nextLevelStart = NULL;
        }
    }
}
