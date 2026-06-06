 class Solution {
    public int[][] reverseSubmatrix(int[][] ki, int x, int y, int k) {

        for (int j = y; j < y + k; j++) {
            Stack<Integer> stk = new Stack<>();
            for(int i=x; i<x+k; i++){
                stk.push(ki[i][j]);
            }
            for(int i=x; i<x+k; i++){
                ki[i][j]=stk.pop();
            }
        }
        return ki;
    }
}