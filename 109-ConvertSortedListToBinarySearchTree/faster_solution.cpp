/**
 * O(n) implementation.
 *
 * Chang Li at UC San Diego
 * Dec. 16, 2015
 */

class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        int len = 0;
        ListNode* pos = head;
        while(pos) {
            len++;
            pos = pos->next;
        }
        return helper(head, 1, len);
    }
    
    TreeNode* helper(ListNode* &head, int start, int end) {
        // Use reference of head
        if(start > end) {
            return NULL;
        }
        int mid = start + (end - start) / 2;
        TreeNode* left = helper(head, start, mid-1);
        TreeNode* root = new TreeNode(head->val);
        head = head->next;
        TreeNode* right = helper(head, mid+1, end);
        root->left = left;
        root->right = right;
        return root;
    }
};
