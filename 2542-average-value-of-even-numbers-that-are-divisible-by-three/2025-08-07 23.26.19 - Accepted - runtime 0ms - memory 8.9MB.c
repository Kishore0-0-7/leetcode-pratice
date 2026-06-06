int averageValue(int* nums, int numsSize) {
    int sum = 0, count = 0;
        for (int n=0;n<numsSize;n++) {
            if (nums[n] % 6 == 0) {
                sum += nums[n];
                count++;
            }
        }
        return count == 0 ? 0 : sum / count;
}