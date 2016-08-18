/**
 * 378. Kth Smallest Element in a Sorted Matrix
 * 
 * Chang Li @ Sunnyvale
 * Aug. 17, 2016
 */
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        priority_queue<int> heap;
        for (int i=0; i<matrix.size(); i++) {
            for (int j=0; j<matrix[i].size(); j++) {
                int element = matrix[i][j];
                if (heap.size() < k) {
                    heap.push(element);
                } else if (heap.top() > element) {
                    heap.pop();
                    heap.push(element);
                } else {
                    break;
                }
            }
        }
        return heap.top();
    }
};
