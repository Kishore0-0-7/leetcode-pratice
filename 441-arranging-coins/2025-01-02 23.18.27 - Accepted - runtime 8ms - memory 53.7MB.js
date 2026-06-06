var arrangeCoins = function(n) {
 let i=0;
        while (i<=n){
            n-=i;
            i+=1;}
        return i-1;   
};