/**
 * 255. Verify Preorder Sequence in Binary Search Tree
 * 
 * Chang Li @ Mountain view
 * Jul. 13, 2016
 */
class Solution {
public:
    bool verifyPreorder(vector<int>& preorder) {
        if (preorder.empty()) return true;
        int pos = 0;
        int mid = preorder[pos++];
        verifyImpl(preorder, pos, 0x80000000, mid);
        verifyImpl(preorder, pos, mid, 0x7FFFFFFF);
        return pos == preorder.size();
    }
    
    void verifyImpl(const vector<int>& vec, int& pos, 
                    int lower_bound, int upper_bound) {
        if (pos == vec.size()) return;
        int mid = vec[pos];
        if (mid < lower_bound || mid > upper_bound) {
            return;
        }
        ++pos;
        verifyImpl(vec, pos, lower_bound, mid);
        verifyImpl(vec, pos, mid, upper_bound);
    }
};
