int maximumDifference(int* nums, int numsSize) {
    int maxso=-1;
        int minso=nums[0];
        for(int i=1;i<numsSize;i++){
            if(nums[i]>minso)
                maxso=maxso>(nums[i]-minso)?maxso:(nums[i]-minso);
            else
                minso=nums[i];
        }
        return maxso;
}