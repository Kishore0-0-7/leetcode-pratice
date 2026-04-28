int maxProfit(int* prices, int pricesSize) {
    int start=prices[0],m=0;
        for(int i=1;i<pricesSize;i++){
            if(start<prices[i]) m+=prices[i]-start;
            start=prices[i];
        }
        return m;
}