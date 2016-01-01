/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 * 
 * Chang Li at Yulin, Shaanxi
 * Jan. 1, 2016
 */
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(k==0 || !head || !(head->next)) return head;
        ListNode dummyNode(0);
        dummyNode.next = head;
        ListNode* dummy = &dummyNode;
        while(true) {
            int count = 0;
            ListNode* end = dummy;
            while(count < k && end != NULL) {
                count ++;
                end = end->next;
            }
            if(end) {
                dummy = reverseList(dummy, end);
            }else {
                break;
            }
        }
        return dummyNode.next;
    }
    
    ListNode* reverseList(ListNode* dummy, ListNode* end) {
        if(end == dummy->next) return end;
        ListNode* first = dummy->next;
        ListNode* second = first->next;
        first->next = end->next;
        dummy->next = end;
        ListNode* newEnd = first;
        while(second != newEnd->next) {
            ListNode* third = second->next;
            second->next = first;
            first = second;
            second = third;
        }
        return newEnd;
    }
};
