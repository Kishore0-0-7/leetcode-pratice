class Solution {
    public int countArrays(int[] original, int[][] bounds) {
        int n = original.length;
        int left = bounds[0][0]; 
        int right = bounds[0][1];
        for (int i = 1; i < n; i++) {
            int diff = original[i] - original[0];
            left = Math.max(left, bounds[i][0] - diff);
            right = Math.min(right, bounds[i][1] - diff);
        }
        return (left <= right) ? right - left + 1 : 0;
    }
}