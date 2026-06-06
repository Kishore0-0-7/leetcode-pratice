/**
 * @param {number[][]} stockPrices
 * @return {number}
 */
var minimumLines=function(A) {
    let n=A.length,res=n-1;
        A.sort((a,b)=>a[0]-b[0]);
        for (let i=1;i<n-1;++i) {
        let x1=BigInt(A[i][0]-A[i-1][0]);
        let y1=BigInt(A[i][1]-A[i-1][1]);
        let x2=BigInt(A[i+1][0]-A[i][0]);
        let y2=BigInt(A[i+1][1]-A[i][1]);
        if (x1 * y2 === x2 * y1) {
            res--;
        }
    }
        return res;
};