/**
 * 359. Logger Rate Limiter
 * 
 * Chang Li @ Mountain View
 * Jun. 19, 2016
 */
class Logger {
public:

    map<string, int> history;

    /** Initialize your data structure here. */
    Logger() {
        
    }
    
    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    bool shouldPrintMessage(int timestamp, string message) {
        auto it = history.find(message);
        if (it == history.end()) {
            history.insert(history.begin(), *(new pair<string, int>(message, timestamp)));
            return true;
        } else if (timestamp - it->second >= 10) {
            it->second = timestamp;
            return true;
        } else {
            return false;
        }
    }
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * bool param_1 = obj.shouldPrintMessage(timestamp,message);
 */
