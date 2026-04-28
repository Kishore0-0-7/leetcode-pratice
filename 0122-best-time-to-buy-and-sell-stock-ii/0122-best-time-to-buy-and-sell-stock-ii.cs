public class Solution {
    public int MaxProfit(int[] prices) {
        int start=prices[0],m=0;
        for(int i=1;i<prices.Length;i++){
            if(start<prices[i]) m+=prices[i]-start;
            start=prices[i];
        }
        return m;
    }
}