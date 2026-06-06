/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let ls=0,rs=0;
       for(let i of nums) rs+=i;
       for (let i=0;i<nums.length;i++){
        rs-=nums[i];
        if(ls==rs) return i;
        ls+=nums[i];
       } 
       return -1;
};