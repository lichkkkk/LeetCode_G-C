/**
 * 369. Plus One Linked List
 * 
 * Chang Li @ Mountain View
 * Jun. 28, 2016
 */
 
/*
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* plusOne(ListNode* head) {
        if (head == nullptr) {
            return head;
        }
        
        head = reverse(head);
        ListNode* curr = head;
        int carry = 1;
        while (true) {
            curr->val += carry;
            carry = curr->val / 10;
            curr->val %= 10;
            if (curr->next == nullptr) {
                break;
            } else {
                curr = curr->next;
            }
        }
        if (carry == 1) {
            curr->next = new ListNode(1);
            curr = curr->next;
        }
        return reverse(head);
    }
    
private:
    ListNode* reverse(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }
        ListNode* first = nullptr;
        ListNode* second = head;
        while (second != nullptr) {
            ListNode* third = second->next;
            second->next = first;
            first = second;
            second = third;
        }
        return first;
    }
};
