/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
    TreeNode* sortedListToBST(ListNode* head) {
        ListNode* slow, * fast, * pre;
        pre = NULL;
        slow = fast = head;
        while(fast && fast->next){
            pre = slow;
            slow = slow->next;
            fast = fast->next;
            if(fast) fast = fast->next;
            else break;
        }
        if(!slow) return NULL;
        auto root = new TreeNode(slow->val);
        root->right = sortedListToBST(slow->next);
        if(pre)pre->next = NULL;
        if(slow == head)root->left = NULL;
        else root->left =  sortedListToBST(head);
        return root;
    }
};
