int findPeakElement(int* nums, int numsSize) {
    int mx = 0;
        for (int i = 1; i < numsSize; i++) {
            if (nums[i] > nums[mx]) {
                mx = i;
            }
        }
        return mx;
}