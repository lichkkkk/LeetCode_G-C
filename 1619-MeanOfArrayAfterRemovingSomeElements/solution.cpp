class Solution {
public:
    double trimMean(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int offset = arr.size() / 20;
        double res = 0;
        for(auto it = arr.begin() + offset; it < arr.end() - offset; it++) {
            res += *it;
        }
        return res /= (arr.size() - offset * 2);
    }
};
