public class Solution {
    public int MaximumDifference(int[] nums) {
        int maxso=-1;
        int minso=nums[0];
        for(int i=1;i<nums.Length;i++){
            if(nums[i]>minso)
                maxso=maxso>(nums[i]-minso)?maxso:(nums[i]-minso);
            else
                minso=nums[i];
        }
        return maxso;
    }
}