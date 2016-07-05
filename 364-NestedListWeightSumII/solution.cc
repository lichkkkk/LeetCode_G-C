/**
 * 364. Nested List Weight Sum II
 * 
 * Chang Li @ Mountain View
 * Jul. 4, 2016
 * 
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class Solution {
public:
    int depthSumInverse(vector<NestedInteger>& nestedList) {
        
        vector<NestedInteger>& list = nestedList;
        vector<int> sum_queue;
        while (!list.empty()) {
            int sum = 0;
            vector<NestedInteger> list_next;
            for (NestedInteger& ni : list) {
                if (ni.isInteger()) {
                    sum += ni.getInteger();
                } else {
                    auto vec = ni.getList();
                    list_next.insert(list_next.end(), vec.begin(), vec.end());
                }
            }
            sum_queue.push_back(sum);
            list = list_next;
        }
        
        int weight = 1;
        int res = 0;
        while (!sum_queue.empty()) {
            res += sum_queue.back() * weight;
            sum_queue.pop_back();
            ++weight;
        }
        return res;
    }
};
