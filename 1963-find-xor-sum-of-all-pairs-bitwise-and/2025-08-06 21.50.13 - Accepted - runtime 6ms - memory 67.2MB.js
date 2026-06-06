/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number}
 */
var getXORSum = function(arr1, arr2) {
    let ans1 = 0;
    let ans2 = 0;
    for (let num of arr1) {
        ans1 ^= num;
    }
    for (let num of arr2) {
        ans2 ^= num;
    }
    return ans1 & ans2;
};