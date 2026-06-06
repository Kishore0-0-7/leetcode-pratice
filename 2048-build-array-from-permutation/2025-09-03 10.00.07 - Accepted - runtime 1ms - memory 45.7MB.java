class Solution {
    public int[] buildArray(int[] nums) {
        int []temp=new int[nums.length];
        int i=0;
        for (int n:nums)
        temp[i++]=nums[n];
        return temp;
    }
}