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
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        binaryMergeKLists( lists );
     }
    inline ListNode *binaryMergeKLists(vector<ListNode *> &lists){
    	if (lists.size() == 0) return NULL;
        else if(lists.size() == 1) return lists[0];
        vector<ListNode *> left_half(lists.begin(), lists.begin()+ lists.size()/2 ),
                           right_half(lists.begin()+ lists.size()/2 , lists.end() );
    	return twoMerge(binaryMergeKLists(left_half), binaryMergeKLists(right_half));
    }
    inline ListNode *twoMerge(ListNode* lHead, ListNode* rHead){
    	if(lHead == NULL) return rHead;
    	if(rHead == NULL) return lHead;
    	ListNode *newHead;
    	ListNode * p , * q;

    	if(lHead->val <= rHead->val ){ p = lHead; q = rHead;}
    	else {p = rHead; q = lHead;}
        newHead = p;
        ListNode * pre;
	    while(p && q){
	        while(p && p->val <= q->val  ){
	        	pre = p;
	            p = p->next; 
	        }     
	        auto t = p;
	        pre->next = q;
	        p = q;
	        q = t;

	    }
	    return newHead;
    	
    }
};
