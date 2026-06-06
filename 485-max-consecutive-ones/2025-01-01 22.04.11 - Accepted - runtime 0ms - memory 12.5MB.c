int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int count = 0;
        int maxCount = 0;
        
        for (int i = 0; i < numsSize; i++) {
            if (nums[i] == 1) {
                count++;
            } else {
                maxCount = fmax(count, maxCount);
                count = 0;
            }
        }
        
        return fmax(count, maxCount);
}