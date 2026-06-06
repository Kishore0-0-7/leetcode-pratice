/**
 * @param {number[]} nums
 * @return {boolean}
 */
var xorGame = function(nums) {
    let x=0;
        for (let i of nums) x^=i;
        return (x==0 || (nums.length&1)==0);
};