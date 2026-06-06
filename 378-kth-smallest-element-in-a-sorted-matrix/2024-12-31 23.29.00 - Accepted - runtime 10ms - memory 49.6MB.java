class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        int[] lst = new int[n * n];
        int index = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                lst[index++] = matrix[i][j];
            }
        }
        Arrays.sort(lst);
        return lst[k - 1];
    }
}