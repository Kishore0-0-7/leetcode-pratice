class Solution {
    public int longestSubarray(int[] nums) {
        int left=0,zero=0,res=0;
        for (int i=0;i<nums.length;i++){
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
    }
}