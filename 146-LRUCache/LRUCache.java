/*
 * HashMap + DoubleLinkedList
 * Running Time: O(1) for both set() and get()
 *
 * Chang Li at UC San Diego
 * Dec. 12, 2015
 */

public class LRUCache {
    
    class ListNode {
        public int key;
        public int val;
        public ListNode prev;
        public ListNode next;
        public ListNode(int key, int value) {
            this.key = key;
            this.val = value;
        }
    }
    
    public final int capacity;
    public int size;
    public ListNode head;
    public ListNode tail;
    
    public boolean putFirst(ListNode node) {
        if(node == head) {
            return true;
        }else {
            if(node == tail) {
                tail = node.prev;
            }else {
                node.next.prev = node.prev;
            }
            node.prev.next = node.next;
            node.next = head;
            head.prev = node;
            node.prev = null;
            head = node;
            return true;
        }
    }
    
    public boolean removeLast() {
        if(size == 0) {
            return false;
        }else if(size == 1){
            map.remove(tail.key);
            head = null;
            tail = null;
            size --;
            return true;
        }else {
            map.remove(tail.key);
            tail.prev.next = null;
            tail = tail.prev;
            size --;
            return true;
        }
    }
    
    public boolean addNewNode(ListNode node) {
        if(size == 0) {
            head = node;
            tail = node;
            size ++;
        }else {
            node.next = head;
            head.prev = node;
            node.prev = null;
            head = node;
            size++;
        }
        return true;
    }
    
    public HashMap<Integer, ListNode> map = new HashMap<>();
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
    }
    
    public int get(int key) {
        if(map.containsKey(key)) {
            ListNode node = map.get(key);
            putFirst(node);
            return node.val;
        }else {
            return -1;
        }
        
    }
    
    public void set(int key, int value) {
        if(map.containsKey(key)) {
            ListNode node = map.get(key);
            putFirst(node);
            node.val = value;
        }else {
            ListNode node = new ListNode(key, value);
            map.put(key, node);
            addNewNode(node);
            if(size > capacity) {
                removeLast();
            }
        }
    }
}
