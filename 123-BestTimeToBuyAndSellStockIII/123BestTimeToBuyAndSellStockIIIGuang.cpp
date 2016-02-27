class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        auto left = maxProfitOnetime(prices.begin(), prices.end());
        auto right = maxProfitOnetimeReverse(prices.rbegin(), prices.rend());
        reverse(right.begin(), right.end());
        for(int i = 0; i < prices.size(); i++)
            profit = max(profit, left[i]+right[i]);
        return profit;
        
    }
    vector<int> maxProfitOnetime(vector<int>::iterator begin,  vector<int>::iterator end) {
        int minPrice = ~(1<<31);
        vector<int> profits;
        int profit = 0;
        for(auto it = begin; it < end; ++it){
            int price = *it;
            profit = max(profit, price-minPrice);
            minPrice = min(minPrice, price);
            profits.push_back(profit);
        }
        return profits;
    }
    vector<int> maxProfitOnetimeReverse(vector<int>::reverse_iterator begin,  vector<int>::reverse_iterator end) {
        int maxPrice = 0;
        vector<int> profits;
        int profit = 0;
        for(auto it = begin; it < end; ++it){
            int price = *it;
            profit = max(profit, maxPrice - price);
            maxPrice = max(maxPrice, price);
            profits.push_back(profit);
        }
        return profits;
    }     
};
