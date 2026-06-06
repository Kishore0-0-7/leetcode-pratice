class Solution {
    public int secondHighest(String s) {
        boolean[] seen=new boolean[10];
        for (char c:s.toCharArray()) {
            if (Character.isDigit(c)) {
                seen[c-'0'] = true;
            }
        }
        int count=0;
        for (int i=9;i>=0;i--) {
            if (seen[i]) {
                count++;
                if (count==2) return i;
            }
        }
        return -1;
    }
}