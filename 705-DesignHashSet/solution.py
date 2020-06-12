class MyHashSet:

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
        
    def add(self, key: int) -> None:
        entry = self.get_entry_(key)
        if key not in entry:
            entry.append(key)

    def remove(self, key: int) -> None:
        entry = self.get_entry_(key)
        if key in entry:
            entry.remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.get_entry_(key)
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
