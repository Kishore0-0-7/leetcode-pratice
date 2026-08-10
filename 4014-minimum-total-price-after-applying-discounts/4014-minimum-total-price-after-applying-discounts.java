class Solution {
    public double minPrice(int[] prices, int[] discounts) {
        Arrays.sort(prices);
        Arrays.sort(discounts);
        double total=0;
        int a=prices.length-1;
        int b=discounts.length-1;
        while(a>=0 && b>=0){
            total+=prices[a]*(100.0-discounts[b])/100.0;
            a--;
            b--;
        }
        while(a>=0){
            total+=prices[a];
            a--;
        }
        return total;
    }
}