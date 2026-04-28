class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int start=prices[0],m=0;
        for(int i=1;i<prices.size();i++){
            if(start<prices[i]) m+=prices[i]-start;
            start=prices[i];
        }
        return m;
    }
};