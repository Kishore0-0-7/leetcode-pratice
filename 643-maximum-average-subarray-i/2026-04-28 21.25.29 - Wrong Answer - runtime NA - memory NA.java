class Solution {
    public double findMaxAverage(int[] nums, int k) {
        float m=0;
        for(int i=0;i<k;i++) m+=nums[i];
        float w=m;
        for(int i=0;i<nums.length-k;i++){
            w=w+nums[i+k]-nums[i];
            m=Math.max(m,w);
        }
        return m/k;
    }
}