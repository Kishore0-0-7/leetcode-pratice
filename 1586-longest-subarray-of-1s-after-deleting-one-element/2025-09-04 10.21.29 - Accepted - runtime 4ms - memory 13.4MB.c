int longestSubarray(int* nums, int numsSize) {
    int left=0,zero=0,res=0;
        for (int i=0;i<numsSize;i++){
            if (nums[i]==0)
                zero+=1;
            while(zero>1){
                if(nums[left]==0)
                    zero-=1;
                left++;
            }
            res=res>(i-left)?res:(i-left);
        }
        return res;
}