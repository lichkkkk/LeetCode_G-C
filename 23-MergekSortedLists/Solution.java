/*
 * If we want to merge two sorted list, it would be easy. If we want 
 * to merge k sorted list, the only issue is that we need to compare
 * more times. So the solution is to use heap.
 *
 * Running time: O(nlogk)
 *
 * Chang Li at UC San Diego
 * Dec. 10, 2015
 */

public class Solution {
	class Node implements Comparable<Node> {
		public ListNode node;
		public Node(ListNode node) {
			this.node = node;
		}
		public int compareTo(Node n) {
			return this.node.val - n.node.val;
		}
	}

    public ListNode mergeKLists(ListNode[] lists) {
    	if(lists == null || lists.length == 0) {
            return null;
        }
        Queue<Node> heap = new PriorityQueue<Node>();
        for(ListNode n : lists) {
        	if(n != null) {
        		heap.offer(new Node(n));
	        }
        }
        ListNode dummy = new ListNode(0);
        ListNode pointer = dummy;
        while(heap.size() > 0) {
        	Node smallest = heap.poll();
        	if(smallest.node.next != null) {
        		heap.offer(new Node(smallest.node.next));
	        }
	        pointer.next = smallest.node;
	        pointer = pointer.next;
        }
        pointer.next = null;
        return dummy.next;
    }
}
