class Solution {
    public int diagonalSum(int[][] mat) {
       int sum=0;
        int c=mat.length;
        for (int i=0;i<c;i++){
            sum +=mat[i][i];
            sum += mat[i][c - 1 - i];
            }
        
        if(c%2==1){
            sum-=mat[c/2][c/2];
        }
        return sum; 
    }
}