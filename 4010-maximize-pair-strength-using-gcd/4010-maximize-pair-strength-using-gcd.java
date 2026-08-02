class Solution {
    public long maxPairStrength(int[] nums) {
        long ans=0;
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                int g=gcd(nums[i],nums[j]);
                long res=1L*nums[i]*nums[j]/(g*g);
                ans=Math.max(ans,res);
            }
        }
        return ans;
    }
    int gcd(int a,int b){
        if(b==0) return a;
        return gcd(b,a%b);
    }
}