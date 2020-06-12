class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.entry_size_ = 100
        self.entry_list_ = [[] for _ in range(self.entry_size_)]
        
    def hash_func_(self, key: int) -> int:
        return key % self.entry_size_;
    
    def get_entry_(self, key: int) -> int:
        entry_index = self.hash_func_(key)
        return self.entry_list_[entry_index]        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        entry = self.get_entry_(key)
        for i in range(len(entry)):
            if entry[i][0] == key:
                entry[i][1] = value
                return
        entry.append([key, value])
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        entry = self.get_entry_(key)
        for i in range(len(entry)):
            if entry[i][0] == key:
                return entry[i][1]
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        entry = self.get_entry_(key)
        pos = -1
        for i in range(len(entry)):
            if entry[i][0] == key:
                pos = i
                break
        if pos != -1:
            entry.pop(pos)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
