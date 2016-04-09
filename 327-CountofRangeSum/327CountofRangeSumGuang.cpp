#define LL long long
struct Node{
    LL L, R;
    int size;
    Node *left, *right;
    Node(LL L, LL R): L(L), R(R), size(0), left(NULL), right(NULL){}
};
class ST{
public:
    ST(LL l, LL r){
        root = new Node(l, r); 
    }
    void add(LL val){
        add(root, val);
    }
    int cnt(LL l, LL r){
        return cnt(root, l, r);
    }
private:
    Node * root;
    int cnt(Node *root, LL l, LL r){
        int res = 0;
        if(root->R < l || root->L > r || l > r)
            return 0;
        if(root->L >= l && root->R <= r)
            return root->size;
        LL M = root->L + (root->R-root->L)/2; // improvements can be applied here. Instead of divide in [L, R], we can use information mid number of L.R in original array
        if(root->left)
            res += cnt(root->left, l, r);
        if(root->right)
            res +=  cnt(root->right, l, r);
        return res;
    }
    void add(Node* root, LL val){ // optimization is applied here. We lazily create new node until necessary so the total space used is O(log(range)(constant)*n).
        ++root->size;
        // not a leaf
        if(root->L != root->R){
            LL M = root->L + (root->R-root->L)/2;
            if(val <= M){
                if(root->left == NULL)
                    root->left = new Node(root->L, M);
                add(root->left, val);
            }else{
                if(root->right == NULL)
                    root->right = new Node(M+1, root->R);
                add(root->right, val);
            }
        }
    }
};
class Solution {
public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        vector<LL> sum;
        sum.push_back(0);
        for(auto n : nums)
            sum.push_back(sum.back()+n);
        ST tree(*min_element(sum.begin(), sum.end()), *max_element(sum.begin(), sum.end()));
        int res = 0;
        tree.add(0);
        for(auto it = sum.begin()+1; it != sum.end(); ++it){
            LL n = *it;
            res += tree.cnt(n-upper, n-lower);
            tree.add(n);
        }
        return res;
    }
};
