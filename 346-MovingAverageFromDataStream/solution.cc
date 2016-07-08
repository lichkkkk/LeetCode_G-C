/**
 * 346. Moving Average from Data Stream
 * 
 * Chang Li @ Mountain View
 * Jul. 7, 2016
 */
class MovingAverage {
public:
    /** Initialize your data structure here. */
    MovingAverage(int size) {
        this->window_size_ = size;
        this->sum_ = 0;
    }
    
    double next(int val) {
        data_stream_.push(val);
        sum_ += val;
        if (data_stream_.size() > window_size_) {
            sum_ -= data_stream_.front();
            data_stream_.pop();
        }
        return sum_ / data_stream_.size();
    }
    
private:
    queue<int> data_stream_;
    double sum_;
    int window_size_;
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */
