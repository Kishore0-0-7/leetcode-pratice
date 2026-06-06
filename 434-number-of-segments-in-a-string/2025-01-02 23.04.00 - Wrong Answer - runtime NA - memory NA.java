class Solution {
    public int countSegments(String s) {
        String[] segments = s.trim().split(" ");
        return s.isEmpty() ? 0 : segments.length;
    }
}