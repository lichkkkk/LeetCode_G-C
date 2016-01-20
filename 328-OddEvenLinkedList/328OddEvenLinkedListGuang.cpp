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
    ListNode* oddEvenList(ListNode* head) {
        auto oddHead = new ListNode(0);
        auto evenHead = new ListNode(0);
        auto oddTail = oddHead;
        auto evenTail = evenHead;
        
        int cnt = 0; // 1 for odd; 
        while(head){
            cnt++;
            //odd
            if(cnt%2){
                oddTail->next = head;
                oddTail = oddTail->next;
            }
            //even
            else{
                evenTail->next = head;
                evenTail = evenTail->next;
            }
            head = head->next;
        }
        oddTail->next = evenHead->next;
        evenTail->next = NULL;
        head = oddHead->next;
        delete oddHead, evenHead;
        return head;
    }
};
