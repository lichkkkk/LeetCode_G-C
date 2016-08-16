/**
 * 135. Candy
 *
 * Chang Li @ Sunnyvale
 */
class Solution {
public:
    int candy(vector<int>& ratings) {
        if (ratings.size() <= 1) return ratings.size();
        vector<int> res(ratings.size(), 1);
        // From left to right
        for (int i=1; i<res.size()-1; ++i) {
            if (ratings[i] > ratings[i-1]) {
                res[i] = res[i-1] + 1;
            }
        }
        res[res.size()-1] = ratings[ratings.size()-1] > ratings[ratings.size()-2] ? res[res.size()-2] + 1 : 1;
        //for (int i : res) cout << i << " "; cout << endl;
        // From right to left
        for (int i=res.size()-2; i>0; --i) {
            if (ratings[i] > ratings[i+1]) {
                res[i] = ratings[i] > ratings[i-1] ? max(res[i+1], res[i-1]) + 1 : res[i+1] + 1;
            }
        }
        res[0] = ratings[0] > ratings[1] ? res[1] + 1 : 1;
        //for (int i : res) cout << i << " "; cout << endl;
        return accumulate(res.begin(), res.end(), 0);
    }
};
