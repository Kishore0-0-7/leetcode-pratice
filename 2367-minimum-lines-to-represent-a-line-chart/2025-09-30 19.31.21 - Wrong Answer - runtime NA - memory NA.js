/**
 * @param {number[][]} stockPrices
 * @return {number}
 */
var minimumLines = function(A) {
    let n=A.length,res=n-1;
        A.sort((a, b) => a[0] - b[0]);
        for (let i=1;i<n-1;++i)
            if ((A[i][0]-A[i-1][0])*(A[i+1][1]-A[i][1])===(A[i+1][0]-A[i][0])*(A[i][1]-A[i-1][1]))
                res--;
        return res;
};