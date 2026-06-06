int pivotIndex(int* nums, int numsSize) {
    int ls=0,rs=0;
       for(int i=0;i<numsSize;i++) rs+=nums[i];
       for (int i=0;i<numsSize;i++){
        rs-=nums[i];
        if(ls==rs) return i;
        ls+=nums[i];
       } 
       return -1;
}