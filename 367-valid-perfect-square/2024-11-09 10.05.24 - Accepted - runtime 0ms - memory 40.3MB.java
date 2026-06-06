class Solution {
    public boolean isPerfectSquare(int num) {
      int a=0;
      a=(int)Math.sqrt(num);
       return Math.pow(a,2)==num; 
    }
}