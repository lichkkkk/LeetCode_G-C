/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 * 
 * 328. Odd Even Linked List
 * Tag: LinkedList, Dummy Node
 * Chang Li at UC San Diego
 * Jan. 19, 2016
 */
public class Solution {
    public ListNode oddEvenList(ListNode head) {
        ListNode odd = new ListNode(0);
        ListNode even = new ListNode(0);
        ListNode currOdd = odd;
        ListNode currEven = even;
        boolean isOdd = true;
        while(head != null) {
            if(isOdd) {
                currOdd.next = head;
                currOdd = currOdd.next;
            }else {
                currEven.next = head;
                currEven = currEven.next;
            }
            isOdd = !isOdd;
            head = head.next;
        }
        currOdd.next = even.next;
        currEven.next = null;
        return odd.next;
    }
}
