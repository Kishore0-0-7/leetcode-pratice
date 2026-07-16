class Solution {
    public long gcdSum(int[] nums) {
        int p[]=new int[nums.length];
        int m=-1;
        for(int i=0;i<nums.length;i++){
            m=Math.max(m,nums[i]);
            p[i]=gcd(m,nums[i]);
        }
        Arrays.sort(p);
        int l=0,r=nums.length-1;
        long sum=0;
        while(l<r){
            sum+=gcd(p[l++],p[r--]);
        }
        return sum;
    }
    int gcd(int a,int b){
        while(b!=0){
            int t=b;
            b=a%b;
            a=t;
        }
        return a;
    }
}
    