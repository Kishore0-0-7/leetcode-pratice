class Solution {
    public String reverseWords(String s) {
        String[] w = s.split(" ");
        StringBuilder rw = new StringBuilder();
        for (int i = w.length - 1; i >= 0; i--) {
            if (!w[i].isEmpty()) {
                rw.append(w[i]).append(" ");
            }
        }
        return rw.toString().trim();
    }
}