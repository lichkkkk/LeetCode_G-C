class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f'{self.key}:{self.val}'

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self._remove_node(self.key_to_node[key])
            self._insert_head_node(node)
            return self.key_to_node[key].val
        else:
            return -1

    def _remove_node(self, node) -> None:
        self.key_to_node.pop(node.key)
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert_head_node(self, node) -> None:
        self.key_to_node[node.key] = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self._remove_node(self.key_to_node[key])
        elif len(self.key_to_node) == self.capacity:
            self._remove_node(self.tail.prev)

        self._insert_head_node(Node(key=key, val=value))

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
