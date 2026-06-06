class Solution {
    public int firstStableIndex(int[] nums, int k) {
        int n=nums.length;
        int px[]=new int[n];
        int sx[]=new int[n];
        px[0]=nums[0];
        sx[n-1]=nums[n-1];
        
        for (int i=1;i<n;i++)
            px[i]=Math.max(px[i-1],nums[i]);

        for(int i=n-2;i>=0;i--)
            sx[i]=Math.min(sx[i+1],nums[i]);

        for(int i=0;i<n;i++)
            if (px[i]-sx[i]<=k) return i;
                
        return -1;
    }
}