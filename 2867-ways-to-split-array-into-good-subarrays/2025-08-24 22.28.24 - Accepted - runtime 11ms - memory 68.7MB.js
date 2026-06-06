/**
 * @param {number[]} nums
 * @return {number}
 */
var numberOfGoodSubarraySplits = function(nums) {
  let cnt = 0;
    let lo = -1;
    const MOD = 1e9 + 7;

    for (let hi = 0; hi < nums.length; hi++) {
        if (nums[hi] === 1) {
            if (cnt === 0) {
                cnt = 1;
            } else {
                cnt = (cnt * (hi - lo)) % MOD;
            }
            lo = hi;
        }
    }
    return cnt;  
};