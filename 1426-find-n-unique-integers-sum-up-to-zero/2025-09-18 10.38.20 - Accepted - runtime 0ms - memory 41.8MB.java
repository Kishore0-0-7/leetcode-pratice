class Solution {
    public int[] sumZero(int n) {
        int[] arr=new int[n];
        int k=1;
        for(int i=0;i<n/2;i++){
            arr[i]=k;
            arr[n-i-1]=-k;
            k++;
        }
        return arr;
    }
}