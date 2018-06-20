/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayPairSum = function(nums) {
    nums.sort(function(a, b){return a - b});
    let res = 0;
    for (i = 0; i< nums.length; i+=2) {
        res += nums[i];
    }
    return res;
};
