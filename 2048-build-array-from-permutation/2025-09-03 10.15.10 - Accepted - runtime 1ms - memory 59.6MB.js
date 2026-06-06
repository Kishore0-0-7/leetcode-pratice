/**
 * @param {number[]} nums
 * @return {number[]}
 */
var buildArray = function(nums) {
    let temp=new Array(nums.length);
    let i=0;
    for(n of nums)
    temp[i++]=nums[n];
    return temp;
};