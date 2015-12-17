/**
 * Use recursion to solve BST problems.
 * Use dummy node.
 *
 * Running Time: O(nlogn) Space: O(h)
 * Chang Li at UC San Diego
 * Dec. 15, 2015
 */

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
        if(head == NULL) {
            return NULL;
        }
        ListNode dummy(0);
        dummy.next = head;
        
        ListNode* slow = &dummy;
        ListNode* fast = slow;
        while(fast->next != NULL && fast->next->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        TreeNode* root = new TreeNode(slow->next->val);
        
        ListNode* first_head = (slow->next == head)? NULL : head;
        ListNode* second_head = slow->next->next;
        slow->next = NULL;
        
        root->left = sortedListToBST(first_head);
        root->right = sortedListToBST(second_head);
        return root;
    }
};
