/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    let left=0,zero=0,res=0;
        for (let i=0;i<nums.length;i++){
            if (nums[i]==0)
                zero+=1;
            while(zero>1){
                if(nums[left]==0)
                    zero-=1;
                left++;
            }
            res=Math.max(res,i-left);
        }
        return res;
};