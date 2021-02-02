class WordDictionary {
    
    private final Trie trie;
    private final Set<String> cache;

    /** Initialize your data structure here. */
    public WordDictionary() {
        trie = new Trie();
        cache = new HashSet<String>();
    }
    
    public void addWord(String word) {
        trie.add(word);
        cache.add(word);
    }
    
    public boolean search(String word) {
        return cache.contains(word) || trie.search(word);
    }
    
    private static class Trie {
        public static class TreeNode {
            public final char ch;
            public final TreeNode[] children;
            public boolean isWordEnd;
            public TreeNode(char ch) {
                this.ch = ch;
                this.children = new TreeNode[26];
                this.isWordEnd = false;
            }
        }

        private final TreeNode root;

        public Trie() {
            root = new TreeNode('#');
        }

        public void add(String word) {
            TreeNode node = root;
            for (char ch : word.toCharArray()) {
                int idx = ch - 'a';
                if (node.children[idx] == null) {
                    node.children[idx] = new TreeNode(ch);
                }
                node = node.children[idx];
            }
            node.isWordEnd = true;
        }

        public boolean search(String word) {
            return subsearch(root, word);
        }
        
        private static boolean subsearch(TreeNode node, String word) {
            for (int i=0; i<word.length(); i++) {
                char ch = word.charAt(i);
                int idx = ch - 'a';
                if (ch == '.') {
                    String subword = word.substring(i+1);
                    for (TreeNode child : node.children) {
                        if (child != null && subsearch(child, subword)) {
                            return true;
                        }
                    }
                    return false;
                } else if (node.children[idx] == null) {
                    return false;
                } else {
                    node = node.children[idx];
                }
            }
            return node.isWordEnd;            
        }
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */
