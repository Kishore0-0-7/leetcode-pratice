/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function(n) {
     let arr=new Array(n);
        let k=1;
        for(let i=0;i<n/2;i++){
            arr[i]=k;
            arr[n-i-1]=-k;
            k++;
        }
        if(n%2==1){
            arr[Math.floor(n/2)]=0;
        }
        return arr;
};