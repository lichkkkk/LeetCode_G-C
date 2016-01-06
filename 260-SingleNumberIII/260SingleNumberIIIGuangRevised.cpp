class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int a, b, aXorb;
        a = b = aXorb = 0;
        for(auto num : nums) aXorb ^= num;
        int lastBit = aXorb & (-aXorb);
        for(auto num : nums){
            if(num & lastBit) a^=num;
        }
        b = a ^ aXorb;
        return vector<int>{a, b};
    }
};
