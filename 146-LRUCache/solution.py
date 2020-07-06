class LRUCache:
    
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.cache = {}
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        if node != self.head:
            # remove node from the linked list
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            if node == self.tail:
                self.tail = node.prev
            # insert it to the head of the list
            node.next = self.head
            node.prev = None
            if self.head:
                self.head.prev = node
            self.head = node
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = self.Node(key, value)
            if len(self.cache) == self.capacity:
                # remove last node from the linked list
                tail_node = self.tail
                if tail_node.prev:
                    tail_node.prev.next = None
                self.tail = tail_node.prev
                del self.cache[tail_node.key]
                del tail_node
            self.cache[key] = node
        else:
            node = self.cache[key]
            node.value = value
            if node == self.head:
                return
            # remove node from the linked list
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            if node == self.tail:
                self.tail = node.prev
        # insert it to the head of the list
        node.next = self.head
        node.prev = None
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node
