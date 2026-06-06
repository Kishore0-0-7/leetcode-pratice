/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sumZero(int n, int* returnSize) {
    int* arr=(int*)malloc(n*sizeof(int));
        int k=1;
        for(int i=0;i<n/2;i++){
            arr[i]=k;
            arr[n-i-1]=-k;
            k++;
        }
        if (n%2==1) {
        arr[n/2]=0;
    }
    *returnSize=n;
        return arr;
}