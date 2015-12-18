


// one way is to use BST


// the other way is to use merge sort as inspiration




class Solution {
public:
    struct cell{
      int val;
      int index;
      int cnt;
      cell(int _val, int _index, int _cnt):val(_val), index(_index), cnt(_cnt){}
    };
    void merge(vector<cell> &s, int start, int mid, int end){
        int start1 = start, start2 = mid+1;
        if(start2 > end) return;
        vector<cell> tmpcell;
        int i = 0, j = 0;
        int len1 = mid-start1 + 1, len2 = end-start2 + 1;
        while(i < len1 && j < len2 ){
            //printf("%d, %d", len1, len2);
            if(s[i+start1].val > s[j+start2].val) {
                s[i+start1].cnt += len2-j;
                tmpcell.push_back(s[i+start1]);
                i++;
            }
            else{
                tmpcell.push_back(s[j+start2]);
                j++;
            }
        }
        while(i < len1){
                tmpcell.push_back(s[i+start1]);
                i++;   
        }
        while(j < len2){
                tmpcell.push_back(s[j+start2]);
                j++;
        }
        for(int k = 0; k < tmpcell.size(); k++)
            s[start+k] = tmpcell[k];
    }
    void sort(vector<cell> &s, int start, int end){
        if(start >= end) return;
        int mid = start + (end-start)/2;
        sort(s, start, mid);
        sort(s, mid+1, end);
        merge(s, start, mid, end);
    }
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> counts(nums.size(), 0);
        vector<cell> s;
        for(int i = 0; i < nums.size(); ++i)
            s.push_back(cell(nums[i], i, 0));
        sort(s, 0, s.size()-1);
        for(int i = 0; i < nums.size(); ++i)
            counts[s[i].index] = s[i].cnt;
        return counts;
    }
};