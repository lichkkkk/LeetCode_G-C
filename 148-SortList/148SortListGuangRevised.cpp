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
        int len = 0;
        auto p = head;
        while(p){
            p = p->next;
            len++;
        }
        //printf("%d \n", len);
        auto fakeHead = new ListNode(0);
        fakeHead->next = head;

        for(int interval = 1; interval < len; interval *= 2){
            //printf("%d interval \n ", interval);
            auto tail = fakeHead;
            while(1){
                if(!(tail->next)) break;
                auto pre = tail;
                auto head1 = tail->next;
                int cnt = interval;
                auto p = head1;
                while(--cnt && p){
                    p = p->next;
                }
                if(!p || !p->next) break;
                ListNode* head2;
                head2 = p->next;
                p->next = NULL;
                cnt = interval;
                p = head2;
                //printf("head2 val, %d\n", head2->val);
                while(--cnt && p){
                    p = p->next;
                }
                //printf("interval, %d\n", interval);
                auto nextHead = p? p->next : p;
                //printf("work\n");
                //printf("p->next-> val in main, %d\n", p->next->val);
                if(p)p->next = NULL;
                pre->next = merge(head1, head2, &tail);
                tail->next = nextHead;
                //printf("tail val in main, %d\n", tail->next);
            }
        }
        auto realHead = fakeHead->next;
        delete fakeHead;
        return realHead;
    }
    
    ListNode *merge(ListNode * left, ListNode * right, ListNode ** pTail){
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
        while(tail->next) tail = tail->next;
        *pTail = tail == head? NULL : tail;
        tail = head->next;
        delete head;
        return tail;
    }
};
