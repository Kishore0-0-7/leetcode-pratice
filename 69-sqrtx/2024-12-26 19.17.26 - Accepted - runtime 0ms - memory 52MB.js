/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    if(x===0) return 0;
       let l=1,h=x,mid=0;
       while(l<=h){
        mid=Math.floor(l+(h-l)/2);
        if (mid*mid ===x)  return mid;
        else if(mid*mid <x) l=mid+1;
        else h=mid-1;
       }
       return h;
};