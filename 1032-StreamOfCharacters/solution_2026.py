class StreamChecker:

    def __init__(self, words: List[str]):
        # construct a trie, each node as a dict
        self.trie = {}
        for w in words:
            if w[0] not in self.trie:
                self.trie[w[0]] = {}
            for i in range(1, len(w)):
                parent = self.trie[w[:i]]
                if w[i] not in parent:
                    new_node = {}
                    parent[w[i]] = new_node
                    self.trie[w[:i+1]] = new_node
            self.trie[w]['#'] = None
        self.curr_nodes = []

    def query(self, letter: str) -> bool:
        new_nodes = []
        has_match = False
        for n in self.curr_nodes:
            if letter in n:
                new_nodes.append(n[letter])
                if '#' in n[letter]:
                    has_match = True
        if letter in self.trie:
            if '#' in self.trie[letter]:
                has_match = True
            new_nodes.append(self.trie[letter])
        self.curr_nodes = new_nodes
        return has_match
        

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
