class Solution {
    public int trap(int[] height) {
        int l=0,r=height.length-1;
        int lm=height[l],rm=height[r];
        int count=0;
        while(l<r){
            if(lm<rm){
                l++;
                lm=Math.max(lm,height[l]);
                count+=lm-height[l];
            }
            else{
                r--;
                rm=Math.max(rm,height[r]);
                count+=rm-height[r];
            }
        }
        return count;
    }
}