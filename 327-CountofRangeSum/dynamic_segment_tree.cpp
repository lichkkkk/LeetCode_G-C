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
    void del(LL val){
        root = del(root, val);
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
        LL M = root->L + (root->R-root->L)/2;
        if(root->left)
            res +=  cnt(root->left, max(l, root->L), min(r, M));
        if(root->right)
            res +=  cnt(root->right, max(l, M+1),    min(r, root->R));
        return res;
    }
    Node* del(Node* root, LL val){
        if(root->size == 0)
            return root;
        // not a leaf
        if(root->L != root->R){
            LL M = root->L + (root->R-root->L)/2;
            if(val <= M){
                root->left = del(root->left, val);
            }else{
                root->right = del(root->right, val);
            }
        }
        --root->size;
        if(root->size == 0){
            delete(root);
            root = NULL;
        }
        return root;
    }
    void add(Node* root, LL val){
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
        for(auto n : sum)
            tree.add(n);
        int res = 0;
        auto it = sum.end()-1;
        while(it != sum.begin()){ // stupid for this special question
            tree.del(*it);
            res += tree.cnt(*it-upper, *it-lower);
            it--;
        }
        return res;
    }
};
