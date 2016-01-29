class Solution {
public:
    const int c = 5;
    int findKthLargest(vector<int>& nums, int k) {
        // sort(nums.begin(), nums.end());
        // return nums[nums.size() - k];
        findKth(nums, 0, nums.size()-1, k);
    }
    int findKth(vector<int>& nums, int start, int end, int k){
        if(end == start) return nums[start];
        int key = findPivotal(nums, start, end);
        int l = start - 1; int h = end + 1;
        while(l < h-1){
            if(nums[l+1] < key){
                --h;
                swap(nums[l+1], nums[h]);
                continue;
            }else{
                l++;
            }
        }
        // start ---- l     <= key
        while(l >= start && nums[l] == key)
            l--;
        int len = l - start + 1;
        
        if(k <= len) return findKth(nums, start, l, k);
        k -= len;
        len = h - l - 1;

        if(k <= len) return key;
        else return findKth(nums, h, end, k-len);
        
    }
    int findPivotal(vector<int>& nums, int start, int end){
        int len = end - start + 1;
        if(len == 1) return nums[start];
        int i = 0;
        while(start + (i+1)*c - 1 <= end){
            insertSort(nums, start+i*c, start+(i+1)*c -1);
            swap(nums[start+i], nums[start+i*c+(c-1)/2]);
            i++;
        }
        if(start+i*c <= end){
            insertSort(nums, start+i*c, end);
            swap(nums[start+i], nums[start+i*c + (end - start-i*c)/2]);
        }
        return findPivotal(nums, start, start+i);
    }
    void insertSort(vector<int>& nums, int start, int end){
        int len = end - start + 1;
        for(int i = start; i <= end -1; i++)
            for(int j = i+1; j <= end; j++){
                if(nums[i] < nums[j])
                    swap(nums[i], nums[j]);
            }
    }
};
