class Solution {
    public void rotate(int[] nums, int k) {
        int n=nums.length;
        k=k%n;
        for (int i=0;i<k;i++)
            help(nums);
    }
    public void help(int []arr){
        int t=arr[arr.length-1];
        for (int i=arr.length-2;i>=0;i--) arr[i+1]=arr[i];
        arr[0]=t;
    }
}