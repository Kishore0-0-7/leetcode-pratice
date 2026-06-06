public class Solution {
    public bool XorGame(int[] nums) {
        int xor=0;
        foreach (int i in nums) xor^=i;
        return (xor==0 || (nums.Length&1)==0);
    }
}