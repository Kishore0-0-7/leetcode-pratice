class Solution {
    public long maxTotalValue(int[] nums, int k) {
        long min=Arrays.stream(nums).min().getAsInt();
        long max=Arrays.stream(nums).max().getAsInt();
        return(max-min)*k;
    }
}