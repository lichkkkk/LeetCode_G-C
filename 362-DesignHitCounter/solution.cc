class HitCounter {
public:
    /** Initialize your data structure here. */
    HitCounter() {}
    
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    void hit(int timestamp) {
        queue_.emplace_back(timestamp);
    }
    
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    int getHits(int timestamp) {
        while (!queue_.empty() && timestamp - queue_.front() >= 300) {
            queue_.pop_front();
        }
        return queue_.size();
    }
private:
    deque<int> queue_;
};
