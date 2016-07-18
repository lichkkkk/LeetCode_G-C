/**
 * 331. Verify Preorder Serialization of a Binary Tree
 * 
 * Chang Li @ Google B47
 * Jul. 16, 2016
 */
class Solution {
public:
    bool isValidSerialization(string preorder) {
        int start_pos = 0;
        matchBinaryTree(preorder, start_pos);
        return start_pos == preorder.size()-1;
    }
    
private:
    void matchBinaryTree(const string& tree, int& start_pos) {
        if (start_pos >= tree.size()) return;
        if (tree[start_pos] == '#') return;
        
        moveToNextNum(tree, start_pos);
        matchBinaryTree(tree, start_pos);
        
        moveToNextNum(tree, start_pos);
        matchBinaryTree(tree, start_pos);
    }
    
    void moveToNextNum(const string& tree, int& start_pos) {
        do { start_pos++; }
        while (start_pos < tree.size()-1 && tree[start_pos+1] != ',');
    }
};
