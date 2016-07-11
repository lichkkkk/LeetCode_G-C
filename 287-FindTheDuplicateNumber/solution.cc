/**
 * 287. Find the Duplicate Number
 * 
 * Chang Li @ Mountain View
 * Jul. 10, 2016
 */
class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int left = 1;
        int right = nums.size()-1;
        while (left+1 < right) {
            int mid = left + (right-left)/2;
            if (count(left, mid, nums) > (mid-left+1)) {
                right = mid;
            } else {
                left = mid;
            }
        }
        return (count(left, left, nums) > 1) ? left : right;
    }
private:
    int count(int from, int to, const vector<int>& nums) {
        int count = 0;
        for (int n : nums) {
            if (n >= from && n <= to) ++count;
        }
        return count;
    }
};
