/**
 * @param {number[]} nums
 * @return {number[]}
 */
var minSubsequence = function(nums) {
    nums.sort((a, b) => b - a);
        let total = nums.reduce((a, b) => a + b, 0);
        let rSum = 0;
        let res = [];

        for (let num of nums) {
            rSum += num;
            res.push(num);
            if (rSum > total - rSum) break;
        }

        return res;
};