/**
 * 339. Nested List Weight Sum
 * 
 * Chang Li @ Mountain View
 * Jul. 10, 2016
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
    int depthSum(vector<NestedInteger>& nestedList) {
        return depthSumImpl(nestedList, 1);
    }
    
    int depthSumImpl(vector<NestedInteger>& nestedList, int weight) {
        int sum = 0;
        for (auto e : nestedList) {
            if (e.isInteger()) {
                sum += e.getInteger() * weight;
            } else {
                sum += depthSumImpl(e.getList(), weight + 1);
            }
        }
        return sum;
    }
};
