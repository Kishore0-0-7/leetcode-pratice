class Solution {
    public void rotate(int[] nums, int k) {
        int n=nums.length;
        k=k%n;
        help(nums,k);
    }
    public void help(int []arr,int k){
        int n=arr.length-k;
        int[] t=new int[k];
        int j=0,a=arr.length-1;
        for (int i=n;i<arr.length;i++) t[j++]=arr[i];
        for (int i=n-1;i>=0;i--){
            arr[a--]=arr[i];
        }
        for(int i=0;i<k;i++) arr[i]=t[i];
    }
}