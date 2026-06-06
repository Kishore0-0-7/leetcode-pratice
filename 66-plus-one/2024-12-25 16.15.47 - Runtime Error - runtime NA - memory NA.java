class Solution {
    public int[] plusOne(int[] digits) {
        StringBuilder num = new StringBuilder();
        for (int digit : digits) {
            num.append(digit);
        }
        int number = Integer.parseInt(num.toString());
        number += 1;
        String result = Integer.toString(number);
        int st[]=new int[result.length()];
        for(int i=0;i<result.length();i++){
            st[i]=result.charAt(i)-'0';
        }
        return st;
    }
}