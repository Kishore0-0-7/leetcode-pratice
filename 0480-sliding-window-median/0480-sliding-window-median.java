class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        int n=nums.length;
        double[] ans=new double[n-k+1];
        List<Integer> window=new ArrayList<>();
        for (int i=0; i < n; i++) {
            int idx=Collections.binarySearch(window, nums[i]);
            if (idx<0) idx=-idx-1;
            window.add(idx, nums[i]);
            if (i>=k-1) {
                if (k%2==1) {
                    ans[i-k+1]=window.get(k/2);
                } else {
                    ans[i-k+1]=((long) window.get(k/2-1)+ window.get(k/2))/2.0;
                }
                idx=Collections.binarySearch(window, nums[i-k+1]);
                window.remove(idx);
            }
        }
        return ans;
    }
}