/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    const d = {};
        for (let i of nums) {
            if (d[i]) {
                return i;
            } else {
                d[i] = 1;
            }
        }
        return -1;
};