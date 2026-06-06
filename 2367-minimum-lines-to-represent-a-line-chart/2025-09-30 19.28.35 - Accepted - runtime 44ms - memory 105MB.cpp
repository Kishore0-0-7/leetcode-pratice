class Solution {
public:
    int minimumLines(vector<vector<int>>& A) {
        int n=A.size(),res= n - 1;
        sort(begin(A),end(A));
        for (int i= 1;i<n-1;i++)
            if (1LL*(A[i][0]-A[i-1][0])*(A[i+1][1]-A[i][1])==1LL*(A[i+1][0]-A[i][0])*(A[i][1]-A[i-1][1]))
                res--;
        return res; 
    }
};