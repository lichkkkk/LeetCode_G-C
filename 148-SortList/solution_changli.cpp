/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 * 
 * 148. Sort List
 * Tag: MergeSort
 * Chang Li at UC San Diego
 * Jan. 10, 2016
 */
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if(head == NULL || head->next == NULL) return head;
        ListNode *head1=NULL, *head2=NULL;
        partitionList(head, &head1, &head2);
        head1 = sortList(head1);
        head2 = sortList(head2);
        return mergeList(head1, head2);
    }
    
    void partitionList(ListNode* head, ListNode** head1, ListNode** head2) {
        ListNode* slow = head;
        ListNode* fast = slow;
        while(fast!=NULL && fast->next!=NULL && fast->next->next!=NULL) {
            fast = fast->next->next;
            slow = slow->next;
        }
        *head1 = head;
        *head2 = slow->next;
        slow->next = NULL;
    }
    
    ListNode* mergeList(ListNode* head1, ListNode* head2) {
        ListNode dummy(0);
        ListNode* head = &dummy;
        while(head1 || head2) {
            if(head1 && head2) {
                if(head1->val < head2->val) {
                    head->next = head1;
                    head = head->next;
                    head1 = head1->next;
                }else {
                    head->next = head2;
                    head = head->next;
                    head2 = head2->next;
                }
            }else if(head1) {
                head->next = head1;
                break;
            }else {
                head->next = head2;
                break;
            }
        }
        return dummy.next;
    }
};
