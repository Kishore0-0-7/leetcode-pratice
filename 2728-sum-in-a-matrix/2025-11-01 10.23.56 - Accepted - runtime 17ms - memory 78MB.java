class Solution {
    public int matrixSum(int[][] nums) {
        int s=0;
        for (int[] arr:nums) Arrays.sort(arr);
        int n=nums.length;
        int m=nums[0].length;
        for (int c=m-1;c>=0;c--){
            int max=0;
            for(int r=0;r<n;r++) max=Math.max(max,nums[r][c]);
            s+=max;
        }
        return s;
    }
}