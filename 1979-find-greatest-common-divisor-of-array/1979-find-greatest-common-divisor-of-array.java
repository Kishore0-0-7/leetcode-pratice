class Solution {
    public int findGCD(int[] nums) {
        int min=1001,max=1;
        for(int i:nums){
            min=Math.min(i,min);
            max=Math.max(i,max);
        }
        return gcd(min,max);
    }
    int gcd(int a,int b){
        while (b!=0){
            int t=b;
            b=a%b;
            a=t;
        }
        return a;
    }
}