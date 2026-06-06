public class Solution {
    public int[] BuildArray(int[] nums) {
        int []temp=new int[nums.Length];
        int i=0;
        foreach(int num in nums)
        temp[i++]=nums[num];
        return temp;
    }
}