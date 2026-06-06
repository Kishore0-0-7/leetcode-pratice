public class Solution {
    public int MinimumLines(int[][] A) {
     int n=A.Length,res=n-1;
        Array.Sort(A,(x,y)=>x[0].CompareTo(y[0]));
        for (int i=1;i<n-1;++i)
            if (1L*(A[i][0]-A[i-1][0])*(A[i+1][1]-A[i][1])==1L*(A[i+1][0]-A[i][0])*(A[i][1]-A[i-1][1]))
                res--;
        return res;   
    }
}