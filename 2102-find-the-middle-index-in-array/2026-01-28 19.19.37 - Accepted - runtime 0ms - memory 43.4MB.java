class Solution {
    public int findMiddleIndex(int[] nums) {
        int a=nums.length;
        int []n=new int[a+1];
        n[0]=0;
        for(int i=0;i<a;i++){
        n[i+1]=nums[i]+n[i];
        }
        for(int i=1;i<=a;i++){
        if(n[a]-n[i]==n[i-1])
        return i-1;
        }
        return -1;
    }
}