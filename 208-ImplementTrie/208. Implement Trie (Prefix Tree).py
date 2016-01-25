__author__ = 'liuxiyun'
# The trie I implement is Ternary tries(cse100 lecture 11 http://cseweb.ucsd.edu/classes/fa15/cse100-a/lectures-ab/Lecture23.pdf)
# Ternary tries avoid the space cost compared with multiway tries

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val=0
        self.isWord=False
        self.left=None
        self.right=None
        self.next=None

class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        self.root.val = 'm'

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        i=0
        # print "root ",node.val
        while i < len(word):
            # print 'cur node ',node.val
            if node.val==0:
                node.val = word[i]
                if i==len(word)-1: # reach the end
                    node.isWord=True
                if node.next == None:
                    node.next = TrieNode()
                node = node.next
                i+=1
            else:
                if word[i] < node.val:
                    if node.left == None:
                        node.left = TrieNode()
                    node=node.left
                elif word[i] > node.val:
                    if node.right == None:
                        node.right = TrieNode()
                    node=node.right
                else:
                    if i==len(word)-1:
                        node.isWord=True
                    if node.next==None:
                        node.next=TrieNode()
                    node=node.next
                    i+=1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur=self.root
        i=0
        while i < len(word):
            if cur == None:
                return False
            if i==len(word)-1 and cur.isWord == True and cur.val == word[i]:
                return True
            if word[i] < cur.val:
                cur=cur.left
            elif word[i] > cur.val:
                cur=cur.right
            else:
                cur=cur.next
                i+=1
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        i=0
        while i < len(prefix):
            if node == None:
                return False
            if prefix[i] < node.val:
                node = node.left
            elif prefix[i] > node.val:
                node = node.right
            else:
                node = node.next
                i+=1
        return True

# Your Trie object will be instantiated and called as such:
# Test case:
# # trie = Trie()
# # trie.insert("a")
# # trie.insert("ab")
# # trie.insert("abcd")
# # trie.insert("zoin")
# # trie.search("x")
# # trie.search("abc")
# # trie.search("abcde")
# # trie.startsWith('ab')