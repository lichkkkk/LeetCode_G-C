/**
 * 341. Flatten Nested List Iterator
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
class NestedIterator {
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        curr_begin_ = nestedList.begin();
        curr_end_ = nestedList.end();
        moveToNextInteger();
    }

    int next() {
        int next = curr_begin_->getInteger();
        curr_begin_ += 1;
        moveToNextInteger();
        return next;
    }

    bool hasNext() {
        if (curr_begin_ == curr_end_) {
            return false;
        } else {
            return true;
        }
    }
private:

    void moveToNextInteger() {
        if (curr_begin_ == curr_end_) {
            if (stack_.empty()) {
                return;
            } else {
                curr_begin_ = stack_.back().first;
                curr_end_ = stack_.back().second;
                stack_.pop_back();
                moveToNextInteger();
            }
        } else {
            if (curr_begin_->isInteger()) {
                return;
            } else {
                stack_.emplace_back(curr_begin_+1, curr_end_);
                curr_end_ = curr_begin_->getList().end();
                curr_begin_ = curr_begin_->getList().begin();
                moveToNextInteger();
            }
        }
    }

    vector<NestedInteger>::iterator curr_begin_;
    vector<NestedInteger>::iterator curr_end_;
    vector<pair<vector<NestedInteger>::iterator, vector<NestedInteger>::iterator>> stack_;
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
