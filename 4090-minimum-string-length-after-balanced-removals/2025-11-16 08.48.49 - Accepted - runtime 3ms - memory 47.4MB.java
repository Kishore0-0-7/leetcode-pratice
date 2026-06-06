class Solution {
    public int minLengthAfterRemovals(String s) {
        int a=0,b=0;
        for (char c:s.toCharArray()){
            if (c=='a') a+=1;
            else b+=1;
        }
        return Math.abs(a-b);
    }
}