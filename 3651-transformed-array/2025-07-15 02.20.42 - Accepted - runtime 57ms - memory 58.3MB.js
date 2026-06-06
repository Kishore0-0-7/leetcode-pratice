/**
 * @param {number[]} nums
 * @return {number[]}
 */
var constructTransformedArray = function(nums) {
    const n = nums.length;
    const res = new Array(n);
    for (let i = 0; i < n; i++) {
        let index = (i + nums[i]) % n;
        if (index < 0) {
            index += n;  // Fix negative index
        }
        res[i] = nums[index];
    }
    return res;
};