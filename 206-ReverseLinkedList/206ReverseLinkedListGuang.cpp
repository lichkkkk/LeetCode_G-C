/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 // kill ing time
 // how boring I am :(
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode * p = NULL;
        while(head && head->next){
            auto q = head->next;
            head->next = p;
            p = head;
            head = q;
        }
        
        if(head) head->next = p;
        
        return head;
    }
};
