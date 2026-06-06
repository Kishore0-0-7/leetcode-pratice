class Solution {
    public int maximumScore(int a, int b, int c) {
        return Math.min((a + b + c) / 2, a + b + c - Math.max(a, Math.max(b, c)));
    }
}