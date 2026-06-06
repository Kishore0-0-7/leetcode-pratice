var trailingZeroes = function(n) {
    let c=0;
        while(n>0){
            n=Math.floor(n/5);
            c+=n;
            }
        return c
};