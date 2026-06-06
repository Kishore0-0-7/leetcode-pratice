class Solution {
    public boolean hasSpecialSubstring(String s, int k) {
        if (k >= s.length()) {
            char first = s.charAt(0);
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) != first) {
                    return false;
                }
            }
            return s.length() == k;
        }

        int i = 0;
        while (i < s.length()) {
            char current = s.charAt(i);
            int j = i + 1;
            while (j < s.length() && s.charAt(j) == current) {
                j++;
            }
            int length = j - i;
            if (length == k) {
                return true;
            }
            i = j;
        }
        return false;
    }
}