/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumXOR = function(nums) {
    let res = 0;
    for (let num of nums) {
        res |= num;
    }
    return res;
};