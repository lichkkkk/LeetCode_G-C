/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 * 
 * 138. Copy List with Random Pointer
 * Tag: HashMap
 * Running Time: O(n)
 * Chang Li at UC San Diego
 * Feb. 5, 2016
 */
 
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        RandomListNode dummy = new RandomListNode(0);
        HashMap<RandomListNode, RandomListNode> map = new HashMap<>();
        RandomListNode oldNode = head;
        RandomListNode newNode = dummy;
        // General Copy
        while (oldNode != null) {
            newNode.next = new RandomListNode(oldNode.label);
            newNode = newNode.next;
            // Store the relationship between old nodes and new nodes
            map.put(oldNode, newNode);
            oldNode = oldNode.next;
        }
        map.put(null, null);
        // Copy the random pointer
        newNode = dummy.next;
        oldNode = head;
        while (oldNode != null) {
            newNode.random = map.get(oldNode.random);
            oldNode = oldNode.next;
            newNode = newNode.next;
        }
        // Return new node
        return dummy.next;
    }
}
