/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* curr_node = head;
        while (curr_node != nullptr) {
            ListNode* next_node = curr_node->next;
            while (next_node != nullptr && next_node->val == curr_node->val) {
                next_node = next_node->next;
            }
            curr_node->next = next_node;
            curr_node = next_node;
        }
        return head;
    }
};

// Not the shortest, but fine
