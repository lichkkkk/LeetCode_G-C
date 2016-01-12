/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if(!head || !(head->next)) return head;
        ListNode * left, *right, *slow, *fast;
        slow = fast = head;
        while(fast && fast->next && fast->next->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        right = sortList(slow->next);
        slow->next = NULL;
        left = sortList(head);
        return merge(left, right);
    }
    
    ListNode *merge(ListNode * left, ListNode * right){
        ListNode *head = new ListNode(0);//dummy node
        ListNode *tail = head;
        while(left || right){
            if(!left){
                 tail->next = right;
                 break;
            }
            if(!right){
                tail->next = left;
                break;
            }
            if(left->val <= right->val){
                tail->next = left;
                left = left->next;
                tail = tail->next;
            }else{
                tail->next = right;
                right = right->next;
                tail = tail->next;
            }
        }
        tail = head->next;
        delete head;
        return tail;
    }
};
