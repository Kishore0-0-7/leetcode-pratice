/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumDifference = function(nums) {
  let maxso=-1;
        let minso=nums[0];
        for(let i=1;i<nums.length;i++){
            if(nums[i]>minso)
                maxso=maxso>(nums[i]-minso)?maxso:(nums[i]-minso);
            else
                minso=nums[i];
        }
        return maxso;  
};